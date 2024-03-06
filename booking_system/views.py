from django.shortcuts import render
from django.views import generic
from .models import Booking
from datetime import date

# Create your views here.
class BookingsList(generic.ListView):
    model = Booking
    queryset = Booking.objects.all()
    template_name = "booking_system/my_account.html"
    paginate_by = 20
    queryset = Booking.objects.filter(date_of_booking__gte=date.today()).order_by('date_of_booking', 'appointment_time')


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