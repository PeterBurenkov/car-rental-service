from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import BookingForm
from .models import *


def bookings(request):
    bookings = Booking.objects.all()
    title = f"All Bookings ({bookings.count()})"
    return render(request, "rental/booking_list.html", {
        "items": bookings,
        'title': title,
    })


def bookings_of_car(request, car_id: int):
    bookings = Booking.objects.filter(car_id=car_id)
    return render(request, "rental/booking_list.html", {
        "items": bookings,
        'title': f"Bookings ({bookings.count()})",
        'title_detail': f'Of Car #{car_id} {Car.objects.get(id=car_id)}'
    })


def bookings_of_customer(request, customer_id: int):
    bookings = Booking.objects.filter(customer_id=customer_id)
    return render(request, "rental/booking_list.html", {
        "items": bookings,
        'title': f"Bookings ({bookings.count()})",
        'title_detail': f'Of Customer #{customer_id} {Customer.objects.get(id=customer_id)}'
    })


class BookingDetailView(generic.DetailView):
    model = Booking


class BookingCreate(CreateView):
    model = Booking
    success_url = reverse_lazy('bookings')
    form_class = BookingForm


class BookingUpdate(UpdateView):
    model = Booking
    success_url = reverse_lazy('bookings')
    form_class = BookingForm


class BookingDelete(DeleteView):
    model = Booking
    success_url = reverse_lazy('bookings')

    def form_valid(self, form):
        try:
            self.object.delete()
            return HttpResponseRedirect(self.success_url)
        except Exception as e:
            return HttpResponseRedirect(
                reverse("booking-delete", kwargs={"pk": self.object.pk})
            )
