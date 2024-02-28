from django.shortcuts import render
from django.views import generic
from .models import Booking


# Create your views here.
class HomeView(generic.ListView):
    queryset = Booking.objects.all()
    template_name = "index.html"