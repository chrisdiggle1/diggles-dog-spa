from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Booking, Services
from datetime import date
from django.contrib.auth.views import LogoutView
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import BookingForm, ServiceForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied


def book_service(request):
    """
    Handles service booking requests. Validates the form on POST,
    checks for past dates or booked slots, and either saves the
    booking or returns an error.
    """
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            service_name = form.cleaned_data['service_name']
            date_of_booking = form.cleaned_data['date_of_booking']
            appointment_time = form.cleaned_data['appointment_time']

            if date_of_booking < timezone.now().date():
                messages.error(
                    request,
                    'You cannot book appointments for dates '
                    'that have already passed.')
                return redirect('book_service')

            existing_appointments = Booking.objects.filter(
                date_of_booking=date_of_booking,
                appointment_time=appointment_time)
            if existing_appointments.exists():
                messages.error(
                    request,
                    'This appointment slot is already booked. '
                    'Please choose a different time.')
                return redirect('book_service')
            booking = form.save(commit=False)
            booking.username = request.user
            booking.save()
            messages.success(
                request, 'Your booking has been successfully made!')
            return redirect('my_account')
    else:
        form = BookingForm()
    return render(request, 'booking_system/book_service.html', {'form': form})


class BookingsList(LoginRequiredMixin, generic.ListView):
    """
    Displays a paginated list of future bookings for the current
    logged-in user.
    """
    model = Booking
    template_name = "booking_system/my_account.html"
    paginate_by = 20

    def get_queryset(self):
        """Override to return bookings for the current user only."""
        return Booking.objects.filter(
            username=self.request.user,
            date_of_booking__gte=date.today()
        ).order_by('date_of_booking', 'appointment_time')


class CustomLogoutView(LogoutView):
    """
    Custom logout view that redirects to the home page after
    logging out and displays a success message.
    """
    next_page = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "You have been successfully logged out.")
        return super().dispatch(request, *args, **kwargs)


@login_required
def edit_booking(request, booking_id):
    """
    Allows a user to edit an existing booking. Validates the edited booking
    details, checks for past dates or conflicting slots, and updates the
    booking. If the edited booking date is in the past or the slot is already
    taken, it returns an error. Changes booking status to 'pending' if it was
    'approved'.
    """
    booking = get_object_or_404(Booking, id=booking_id)
    if booking.username != request.user:
        raise PermissionDenied

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            date_of_booking = form.cleaned_data['date_of_booking']
            if date_of_booking < timezone.now().date():
                messages.error(request,
                               'You cannot set a booking for dates that have '
                               'already passed.')
                return render(request, 'booking_system/edit_booking.html',
                              {'form': form})

            appointment_time = form.cleaned_data['appointment_time']
            existing_appointments = Booking.objects.exclude(
                id=booking_id).filter(date_of_booking=date_of_booking,
                                      appointment_time=appointment_time)
            if existing_appointments.exists():
                messages.error(request,
                               'This appointment slot is already booked. '
                               ' Please choose a different time.')
                return render(request, 'booking_system/edit_booking.html',
                              {'form': form})

            if booking.status == 'approved':
                booking.status = 'pending'
                booking.save()
                messages.success(request,
                                 'Booking updated successfully. It is now '
                                 'pending approval.')
                return redirect('my_account')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'booking_system/edit_booking.html', {'form': form})


@login_required
def cancel_booking(request, booking_id):
    """
    Cancels an existing booking if the logged-in user is the owner. Deletes
    the booking and displays a success message.
    """
    booking = get_object_or_404(Booking, id=booking_id)
    if booking.username != request.user:
        raise PermissionDenied

    booking.delete()
    messages.success(request, 'Booking cancelled successfully.')
    return redirect('my_account')


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def price_list(request):
    services = Services.objects.all()
    return render(request, 'price_list.html', {'services': services})


def register(request):
    return render(request, 'account/signup.html')


def login(request):
    return render(request, 'account/login.html')


def logout(request):
    return render(request, 'account/logout.html')


def is_superuser(user):
    return user.is_authenticated and user.is_superuser


@login_required
@user_passes_test(is_superuser)
def dashboard(request):
    """
    Renders the admin dashboard with lists of bookings and services.
    Seperates bookings into approved and rejected bookings,
    pending approvals, and services the business offers.
    """
    bookings = Booking.objects.exclude(status='pending')
    pending_approvals = Booking.objects.filter(status='pending')
    approved_bookings = Booking.objects.filter(status='approved')
    services = Services.objects.all()
    return render(request, 'booking_system/admin_dashboard.html', {
        'bookings': bookings,
        'pending_approvals': pending_approvals,
        'approved_bookings': approved_bookings,
        'services': services
    })


@login_required
@user_passes_test(is_superuser)
def approve_booking(request, booking_id):
    """
    Approves a pending booking based on its ID. Sets the booking
    status to 'approved', saves the changes, and displays a success
    message.
    """
    booking = get_object_or_404(Booking, id=booking_id)
    booking.status = 'approved'
    booking.save()
    messages.success(request, 'Booking approved successfully.')
    return redirect('dashboard')


@login_required
@user_passes_test(is_superuser)
def reject_booking(request, booking_id):
    """
    Rejects a pending booking based on its ID by setting the booking
    status to 'rejected', saves the update, and displays a success
    message to the administrator.
    """
    booking = get_object_or_404(Booking, id=booking_id)
    booking.status = 'rejected'
    booking.save()
    messages.success(request, 'Booking rejected successfully.')
    return redirect('dashboard')


@login_required
@user_passes_test(is_superuser)
def add_service(request):
    """
    Allows the admin to add a new service. On POST, validates the service
    form, saves the new service if valid, displays a success message, and
    redirects to the dashboard, otherwsie displays the form for adding a
    service.
    """
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Service added successfully.')
            return redirect('dashboard')
    else:
        form = ServiceForm()
    return render(request, 'booking_system/add_service.html', {'form': form})


@login_required
@user_passes_test(is_superuser)
def delete_service(request, service_id):
    """
    Deletes a specific service identified by its ID. Notifies the
    adminstrator of successful deletion with a message and redirects
    to the dashboard.
    """
    service = Services.objects.get(id=service_id)
    service.delete()
    messages.success(request, 'Service deleted successfully.')
    return redirect('dashboard')
