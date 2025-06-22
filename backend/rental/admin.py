from djangoql.admin import DjangoQLSearchMixin
from django.contrib import admin

# Register your models here.

from .models import *


class CarAdmin(DjangoQLSearchMixin, admin.ModelAdmin):
    list_display = [field.name for field in Car._meta.fields]
    search_fields = ['color', 'year', 'millage']


class CarModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CarModel._meta.fields]


class CustomerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Customer._meta.fields]
    search_fields = [field.name for field in Customer._meta.fields]


class BookingAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Booking._meta.fields]


for model_class, admin_class in [
    (Car, CarAdmin),
    (CarModel, CarModelAdmin),
    (Customer, CustomerAdmin),
    (Booking, BookingAdmin),
]:
    admin.site.register(model_class, admin_class)

