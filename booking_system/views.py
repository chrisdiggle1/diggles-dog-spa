from django.shortcuts import render, redirect
from django.views import generic
from .models import Booking, Services
from datetime import date
from django.contrib.auth.views import LogoutView
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import BookingForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


def book_service(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.username = request.user
            booking.save()
            messages.success(
                request, 'Your booking has been successfully made!')
            return redirect('home')
    else:
        form = BookingForm()
    return render(request, 'booking/book_service.html', {'form': form})


class BookingsList(LoginRequiredMixin, generic.ListView):
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
    next_page = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "You have been successfully logged out.")
        return super().dispatch(request, *args, **kwargs)


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
