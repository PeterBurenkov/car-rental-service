from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import *


def car_models(request):
    items = CarModel.objects.all()
    return render(request, "rental/carModel_list.html", {"items": items})


def cars_of_model(request, model_id: int):
    model = CarModel.objects.get(id=model_id)
    cars = Car.objects.filter(model=model_id)
    return render(request, "rental/car_list.html", {
        "items": cars,
        'title': f"Cars ({cars.count()})",
        'title_detail': f"Of Model #{model_id} {model}"
    })


class CarModelDetailView(generic.DetailView):
    model = CarModel


class CarModelCreate(CreateView):
    model = CarModel
    fields = ['make', 'model', 'series']
    success_url = reverse_lazy('car-models')


class CarModelUpdate(UpdateView):
    model = CarModel
    fields = '__all__'
    success_url = reverse_lazy('car-models')


class CarModelDelete(DeleteView):
    model = CarModel
    success_url = reverse_lazy('car-models')

    def form_valid(self, form):
        try:
            self.object.delete()
            return HttpResponseRedirect(self.success_url)
        except Exception as e:
            return HttpResponseRedirect(
                reverse("car-model-delete", kwargs={"pk": self.object.pk})
            )
