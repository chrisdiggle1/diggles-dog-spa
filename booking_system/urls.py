from . import views
from django.urls import path, include
from .views import BookingsList

urlpatterns = [
    path("", views.home, name='home'),
    path('about/', views.about, name='about'),
    path('price-list/', views.price_list, name='price_list'),
    path('accounts/', include('allauth.urls')),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('my-account/', views.BookingsList.as_view(), name='my_account'),
    path('book-service/', views.book_service, name='book_service'),
    path('edit-booking/<int:booking_id>/',
         views.edit_booking, name='edit_booking'),
    path('cancel-booking/<int:booking_id>/',
         views.cancel_booking, name='cancel_booking'),
]
