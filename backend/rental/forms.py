from django import forms
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.forms import ModelForm

from .models import Booking


class DateInput(forms.DateInput):
    input_type = 'date'


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['car', 'customer', 'date_from', 'date_to']
        widgets = {
            'date_from': DateInput(),
            'date_to': DateInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        a = cleaned_data.get("date_from")
        b = cleaned_data.get("date_to")
        car = cleaned_data.get("car")

        id = self.instance.pk

        if a > b:
            raise ValidationError(
                ["`Date from` should be earlier than `Date to`"]
            )

        # todo cover with unit tests
        overlapping_bookings = Booking.objects.filter(
            ~Q(id=id) &  # exclude current booking
            Q(car_id=car.id) &  # the same car
            (
                    Q(date_from__lte=a) & Q(date_to__gte=b) |  # current period inside other completely
                    Q(date_from__gte=a) & Q(date_to__lte=b) |  # other period inside current completely
                    Q(date_from__lte=a) & Q(date_to__gte=a) |  # left limit of current inside the other
                    Q(date_from__lte=b) & Q(date_to__gte=b) |  # right limit of current inside the other
                    Q(date_from__gte=a) & Q(date_from__lte=b) |  # left limit of other inside the current
                    Q(date_to__gte=a) & Q(date_to__lte=b)  # right limit of other inside the current
            )
        )

        if overlapping_bookings.count() > 0:
            ids = ', '.join([f'#{x.id}' for x in overlapping_bookings])
            raise ValidationError(
                f"Overlapping periods with booking {ids}"
            )
