from django.test import TestCase
from django.contrib.auth.models import User
from .models import Services, Booking
from datetime import timedelta, date, time


class ServicesModelTest(TestCase):
    """
    Tests the funcionality of the Services model.
    """

    def test_services_creation(self):
        """
        Tests if a Services instance is correctly made with the right details.
        """
        service = Services.objects.create(
            service_name="Eye Cleaning",
            cost="All Sizes: £10",
            description="Cleaning around the eyes to remove tear stains.",
            duration=timedelta(hours=1, minutes=30)
        )
        self.assertTrue(isinstance(service, Services))
        self.assertEqual(str(service), "Eye Cleaning")
        self.assertEqual(service.formatted_duration(), "1h 30min")


class BookingModelTest(TestCase):
    """
    Tests the funcionality of the Booking model.
    """

    def setUp(self):
        """
        Creates a user and service instance to test booking creation.
        """
        self.user = User.objects.create_user(
            username='testuser', password='12345')
        self.service = Services.objects.create(
            service_name="Eye Cleaning",
            cost="All Sizes: £10",
            description="Cleaning around the eyes to remove tear stains.",
            duration=timedelta(hours=1, minutes=30)
        )

    def test_booking_creation(self):
        """
        Tests that a booking instance can be created and associated with
        the correct user and service.
        """
        booking_date = date.today()
        booking = Booking.objects.create(
            username=self.user,
            dog_name="Marley",
            dog_breed="Cavapoochon",
            service_name=self.service,
            date_of_booking=booking_date,
            appointment_time=time(14, 30),
            confirmed=True,
            status='pending'
        )
        self.assertTrue(isinstance(booking, Booking))

        expected_str = (f"{self.service} for Marley on "
                        f"{booking_date} at 14:30:00")
        self.assertEqual(str(booking), expected_str)
        self.assertEqual(booking.status, 'pending')
