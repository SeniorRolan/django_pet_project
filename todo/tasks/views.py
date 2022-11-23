from django.shortcuts import render
from .models import Truck
from .forms import TruckForm
from django.db.models import F


def tasks_list(request):
    if request.method == 'POST':
        form = TruckForm
        tasks = Truck.objects.all().annotate(overload=(F('current_cargo') - F('truck_model__load_capacity')) * 100 / F('truck_model__load_capacity'))
        if form.is_valid:
            return render(request, 'tasks/tasks_list.html', {'form': form, 'tasks': tasks})
    else:
        tasks = Truck.objects.all().annotate(overload=(F('current_cargo') - F('truck_model__load_capacity')) * 100 / F('truck_model__load_capacity'))
        form = TruckForm
    return render(request, 'tasks/tasks_list.html', {'form': form, 'tasks': tasks})



