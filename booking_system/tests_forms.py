from django.contrib.auth.models import User
from django.test import TestCase
from .forms import BookingForm, ServiceForm
from .models import Services
from datetime import datetime, timedelta, time

class BookingFormTest(TestCase):
    """
    This tests the BookingForm for validation and creates a booking.
    """

    def setUp(self):
        """ 
        Prepares the test user and a service instance for form testing.
        """
        self.user = User.objects.create_user('testuser', 'test@example.com', 'testpassword')
        self.service = Services.objects.create(
            service_name="Grooming Basic",
            cost="50",
            description="Basic grooming service",
            duration=timedelta(hours=0, minutes=30)
        )

    def test_booking_form_validity(self):
        """
        Ensures the BookingForm validates and correctly creates a booking. 
        """
        form_data = {
            'dog_name': 'Marley',
            'dog_breed': 'Cavapoochon',
            'service_name': self.service.id,
            'date_of_booking': datetime.today().date(),
            'appointment_time': time(12, 0)
        }

        form = BookingForm(data=form_data)
        self.assertTrue(form.is_valid())

        booking = form.save(commit=False)
        booking.username = self.user
        booking.save()

        self.assertEqual(booking.dog_name, 'Marley')
        self.assertEqual(booking.dog_breed, 'Cavapoochon')
