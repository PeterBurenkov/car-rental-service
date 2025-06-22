from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import *


def cars(request):
    cars = Car.objects.all()
    return render(request, "rental/car_list.html", {
        "items": cars,
        'title': f"All Cars ({cars.count()})"
    })


class CarDetailView(generic.DetailView):
    model = Car


class CarCreate(CreateView):
    model = Car
    fields = ['model', 'color', 'year', 'millage']
    success_url = reverse_lazy('cars')


class CarUpdate(UpdateView):
    model = Car
    fields = '__all__'
    success_url = reverse_lazy('cars')


class CarDelete(DeleteView):
    model = Car
    success_url = reverse_lazy('cars')

    def form_valid(self, form):
        try:
            self.object.delete()
            return HttpResponseRedirect(self.success_url)
        except Exception as e:
            return HttpResponseRedirect(
                reverse("car-delete", kwargs={"pk": self.object.pk})
            )
