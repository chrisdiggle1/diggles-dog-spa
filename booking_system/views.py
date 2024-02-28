from django.shortcuts import render
from django.views import generic
from .models import Booking


# Create your views here.
class HomeView(generic.ListView):
    queryset = Booking.objects.all()
    template_name = "index.html"


def about(request):
    return render(request, 'about.html')

def price_list(request):
    return render(request, 'price_list.html')

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')