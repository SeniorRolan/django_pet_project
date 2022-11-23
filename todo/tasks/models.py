from django.db import models
from model_utils.models import TimeStampedModel


class TruckModel(TimeStampedModel):
    name = models.CharField(verbose_name='Название модели', max_length=255)
    load_capacity = models.SmallIntegerField(verbose_name='Грузоподъёмность', null=True)

    def __str__(self):
        return self.name


class Truck(TimeStampedModel):
    side_number = models.CharField(verbose_name='Бортовой номер', max_length=255, unique=True, null=True)
    truck_model = models.ForeignKey(TruckModel, related_name='model', verbose_name='Модель самосвала', on_delete=models.CASCADE, null=True)
    current_cargo = models.SmallIntegerField(verbose_name='Текущая загруженность', null=True)

    def __str__(self):
        return self.current_cargo
