from django.db import models
from django.contrib.auth.models import User
import datetime


STATUS = ((0, "Pending"), (1, "Confirmed"))

BOOKING_TIME = ((datetime.time(9, 0, 0), '9:00am'),
                (datetime.time(9, 30, 0), '9:30am'),
                (datetime.time(10, 0, 0), '10:00am'),
                (datetime.time(10, 30, 0), '10:30am'),
                (datetime.time(11, 0, 0), '11:00am'),
                (datetime.time(11, 30, 0), '11:30am'),
                (datetime.time(12, 0, 0), '12:00pm'),
                (datetime.time(12, 30, 0), '12:30pm'),
                (datetime.time(13, 0, 0), '1:00pm'),
                (datetime.time(13, 30, 0), '1:30pm'),
                (datetime.time(14, 0, 0), '2:00pm'),
                (datetime.time(14, 30, 0), '2:30pm'),
                (datetime.time(15, 0, 0), '3:00pm'),
                (datetime.time(15, 30, 0), '3:30pm'),
                (datetime.time(16, 0, 0), '4:00pm'),
                (datetime.time(16, 30, 0), '4:30pm'),
                )


class Services(models.Model):
    """
    Model representing the services offered, detailing the service's name, 
    cost, description and the estimated duration.

    `__str__`: Human-readable string representation of the service.

    `return self.service_name` A string representing the name of the service.
    """
    service_name = models.CharField(max_length=100)
    cost = models.TextField(
        help_text="Enter the cost range depending on dog size, e.g., 'Small Dogs: £35, Large Dogs: £100'")
    description = models.CharField(max_length=500, blank=True)
    duration = models.DurationField(
        help_text="Estimated duration of the service")

    def formatted_duration(self):
        total_seconds = self.duration.total_seconds()
        hours = int(total_seconds // 3600)
        minutes = int((total_seconds % 3600) // 60)
        return f"{hours}h {minutes}min"

    class Meta:
        ordering = ['service_name', 'description', 'cost', 'duration']

    def __str__(self):
        return self.service_name


class Booking(models.Model):
    """
    Model representing a booking made by the user, including  details about the user, 
    their dog the service booked and the appointment timing.

    `__str__`: Human-readable string representation of the booking.
    """
    username = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='username_booking')
    dog_name = models.CharField(max_length=100)
    dog_breed = models.CharField(max_length=100, blank=True, null=True)
    service_name = models.ForeignKey(
        Services, on_delete=models.CASCADE, related_name='service_name_booking')
    date_of_booking = models.DateField()
    appointment_time = models.TimeField(choices=BOOKING_TIME)
    confirmed = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['service_name', 'date_of_booking', 'appointment_time']

    def __str__(self):
        return (f"{self.service_name} for {self.dog_name} "
                f"on {self.date_of_booking} at {self.appointment_time}")
