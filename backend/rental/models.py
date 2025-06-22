from django.db import models
from django.urls import reverse
from datetime import timedelta


class CarModel(models.Model):
    make = models.CharField(max_length=200, null=True, blank=True)
    model = models.CharField(max_length=200, null=True, blank=True)
    series = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        attributes = [self.make, self.model, self.series]
        attributes = [str(x) for x in attributes if x is not None]
        return ' '.join(attributes)


class Car(models.Model):
    class Color(models.TextChoices):
        white = 'white'
        black = 'black'
        blue = 'blue'
        red = 'red'

    model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    color = models.CharField(max_length=200, null=True, blank=True, choices=Color.choices)
    year = models.IntegerField(null=True, blank=True)
    millage = models.FloatField(null=True, blank=True)


    def __str__(self):
        attributes = [self.model, self.color, self.year]
        attributes = [str(x) for x in attributes if x is not None]
        return ' | '.join(attributes)


class Customer(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        attributes = [self.name, self.email, self.phone]
        attributes = [str(x) for x in attributes if x is not None]
        return ' | '.join(attributes)

    def get_absolute_url(self):
        return reverse('customer-detail', args=[str(self.id)])


class Booking(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_from = models.DateField("rent from date (inclusive)")
    date_to = models.DateField("rent to date (inclusive)")

    def days(self) -> int:
        return abs((self.date_to - self.date_from).days) + 1

    def date_from_for_chart(self):
        return self.date_from - timedelta(days=1)

    def __str__(self):
        attributes = [self.car, self.customer, f'from [{self.date_from}, to {self.date_to}]']
        attributes = [str(x) for x in attributes if x is not None]
        return ' -> '.join(attributes)


