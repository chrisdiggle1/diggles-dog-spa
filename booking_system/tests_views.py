from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Services
from datetime import datetime, timedelta


class BookServiceViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='secret'
        )
        self.service = Services.objects.create(
            service_name="Eye Cleaning",
            cost="10",
            description="Cleaning around the eyes to remove tear stains.",
            duration=timedelta(minutes=30)
        )
        self.url = reverse('book_service')

    def test_book_service_get(self):
        """
        Test the book_service view returns the correct template for
        GET requests.
        """
        self.client.login(username='testuser', password='secret')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking_system/book_service.html')

    def test_book_service_post_success(self):
        """
        Test successful booking creation through the book_service view.
        """
        self.client.login(username='testuser', password='secret')
        booking_date = (datetime.now() + timedelta(days=1)).date()
        response = self.client.post(self.url, {
            'dog_name': 'Marley',
            'dog_breed': 'Cavapoochon',
            'service_name': self.service.id,
            'date_of_booking': booking_date,
            'appointment_time': '09:00:00'
        })
        self.assertRedirects(response, reverse(
            'my_account'), status_code=302, target_status_code=200)

    def test_bookings_list_view(self):
        """
        Test that the BookingsList view correctly restricts access to logged-in
        users and displays user-specific bookings.
        """
        response = self.client.get(reverse('my_account'))
        self.assertEqual(response.status_code, 302)
        self.client.login(username='testuser', password='secret')
        response = self.client.get(reverse('my_account'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking_system/my_account.html')

    def test_home_view(self):
        """
        Test the home view to ensure it uses the correct template.
        """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
