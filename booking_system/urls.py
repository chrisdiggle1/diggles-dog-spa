from . import views
from django.urls import path
from .views import BookingsList

urlpatterns = [
    path("", views.BookingsList.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('price-list/', views.price_list, name='price_list'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('my-account/', views.BookingsList.as_view(), name='my_account'),
]