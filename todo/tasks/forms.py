from django import forms
from .models import TruckModel, Truck


class TruckForm(forms.Form):

    truck_model = forms.ModelChoiceField(queryset=TruckModel.objects.all().distinct().values_list('name', flat=True),
                                         empty_label='Все', label='Модель')
