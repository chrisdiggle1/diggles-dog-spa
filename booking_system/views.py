from django.shortcuts import render
from django.views import generic
from .models import Booking
from datetime import date
from django.contrib.auth.views import LogoutView
from django.contrib import messages
from django.urls import reverse_lazy

# Create your views here.
class BookingsList(generic.ListView):
    model = Booking
    queryset = Booking.objects.all()
    template_name = "booking_system/my_account.html"
    paginate_by = 20
    queryset = Booking.objects.filter(date_of_booking__gte=date.today()).order_by('date_of_booking', 'appointment_time')

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
    return render(request, 'price_list.html')

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'account/login.html')

def logout(request):
    return render(request, 'account/logout.html')