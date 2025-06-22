from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import *


def customers(request):
    items = Customer.objects.all()
    return render(request, "rental/customer_list.html", {"items": items})


class CustomerDetailView(generic.DetailView):
    model = Customer


class CustomerCreate(CreateView):
    model = Customer
    fields = ['name', 'email', 'phone']
    initial = {'name': 'new_customer'}
    success_url = reverse_lazy('customers')


class CustomerUpdate(UpdateView):
    model = Customer
    fields = '__all__'
    success_url = reverse_lazy('customers')


class CustomerDelete(DeleteView):
    model = Customer
    success_url = reverse_lazy('customers')

    def form_valid(self, form):
        try:
            self.object.delete()
            return HttpResponseRedirect(self.success_url)
        except Exception as e:
            return HttpResponseRedirect(
                reverse("customer-delete", kwargs={"pk": self.object.pk})
            )
