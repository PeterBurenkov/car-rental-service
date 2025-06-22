from datetime import datetime

from django.db.models import Q
from django.http import HttpResponse
from django.template import loader

from .models import *


def index(request):
    today = datetime.today()
    active_bookings_count = Booking.objects.filter(Q(date_from__lte=today) & Q(date_to__gte=today)).count()
    future_bookings_count = Booking.objects.filter(Q(date_from__gte=today)).count()

    carModels = CarModel.objects.all()
    cars = Car.objects.all()
    customers = Customer.objects.all()
    bookings = Booking.objects.all()
    template = loader.get_template('rental/index.html')
    cars_without_bookings = Car.objects.filter(booking__isnull=True)
    context = {
        'carModels': carModels,
        'cars': cars,
        'customers': customers,
        'bookings': bookings,
        'active_bookings_count': active_bookings_count,
        'future_bookings_count': future_bookings_count,
        'cars_without_bookings': cars_without_bookings,
        'min_date': Booking.objects.earliest('date_from').date_from_for_chart,
        'max_date': Booking.objects.latest('date_to').date_to
    }
    return HttpResponse(template.render(context, request))
