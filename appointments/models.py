from django.db import models

class Appointment(models.Model):
    customer_name = models.CharField(max_length=255)
    service = models.CharField(max_length=255)
    appointment_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} - {self.service} on {self.appointment_date}"
