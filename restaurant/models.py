from django.db import models

class Menu(models.Model):
    id = models.AutoField(primary_key=True)  # Use AutoField with primary_key=True
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.SmallIntegerField()  # Remove max_length

    def __str__(self):
        return self.title


class Booking(models.Model):
    id = models.AutoField(primary_key=True)  # Use AutoField with primary_key=True
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()  # Remove max_length
    bookingdate = models.DateField()

    def __str__(self):
        return self.name


# Create your models here.
