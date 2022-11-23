from django import forms
from .models import TruckModel, Truck


class TruckForm(forms.Form):

    truck_model = forms.ModelChoiceField(queryset=TruckModel.objects.all().values('name').distinct(), empty_label='Все',
                                         label='Модель')

