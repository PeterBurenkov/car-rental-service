from djangoql.admin import DjangoQLSearchMixin
from django.contrib import admin

# Register your models here.

from .models import *


class CarAdmin(DjangoQLSearchMixin, admin.ModelAdmin):
    list_display = [field.name for field in Car._meta.fields]
    search_fields = list_display

class CarModelAdmin(DjangoQLSearchMixin, admin.ModelAdmin):
    list_display = [field.name for field in CarModel._meta.fields]
    search_fields = list_display


class CustomerAdmin(DjangoQLSearchMixin, admin.ModelAdmin):
    list_display = [field.name for field in Customer._meta.fields]
    search_fields = list_display


class BookingAdmin(DjangoQLSearchMixin, admin.ModelAdmin):
    list_display = [field.name for field in Booking._meta.fields]
    search_fields = list_display


for model_class, admin_class in [
    (Car, CarAdmin),
    (CarModel, CarModelAdmin),
    (Customer, CustomerAdmin),
    (Booking, BookingAdmin),
]:
    admin.site.register(model_class, admin_class)

