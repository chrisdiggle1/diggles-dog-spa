from . import views
from django.urls import path


urlpatterns = [
    path("", views.HomeView.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('price-list/', views.price_list, name='price_list'),
    path('register/', views.register, name='register'),
    path('login/', views.register, name='login'),
]