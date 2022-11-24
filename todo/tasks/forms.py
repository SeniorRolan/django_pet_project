from django import forms
from .models import TruckModel, Truck


class TruckForm(forms.Form):
    queryset = TruckModel.objects.all().distinct().values_list('name', flat=True)
    truck_model = forms.ModelChoiceField(queryset=queryset, empty_label='Все', label='Модель')
