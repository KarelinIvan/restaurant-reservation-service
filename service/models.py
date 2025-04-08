from datetime import timedelta

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models


class Table(models.Model):
    """ Модель для выбора столика """

    class Location(models.TextChoices):
        """ Класс для выбора расположения столика """
        HALL = 'HL', 'Зал у окна'
        TERRACE = 'TR', 'Терраса'

    name = models.IntegerField(verbose_name='Номер столика', unique=True)
    seats = models.IntegerField(verbose_name='Количество мест', validators=[MinValueValidator(1)])
    location = models.CharField(max_length=2, choices=Location.choices, verbose_name='Расположение столика')

    class Meta:
        verbose_name = 'Столик'
        verbose_name_plural = 'Столики'
        ordering = ['name', ]

    def __str__(self):
        return f'{self.name} ({self.seats} seats) - {self.location}'


class Reservation(models.Model):
    """ Модель для бронирования """
    customer_name = models.CharField(max_length=200, verbose_name='Фамилия Имя бронирующего')
    table_id = models.ForeignKey(Table, on_delete=models.CASCADE)
    reservation_time = models.DateTimeField(verbose_name='Дата и время бронирование столика')
    duration_minutes = models.IntegerField(verbose_name='Продолжительность брони')

    class Meta:
        verbose_name = 'Бронь'
        verbose_name_plural = 'Бронь'

    def clean(self):
        # Проверка на пересечение бронирования
        overlapping_reservations = Reservation.objects.filter(
            table_id=self.table_id,
            reservation_time__lt=self.reservation_time + timedelta(minutes=self.duration_minutes),
            reservation_time__gt=self.reservation_time - timedelta(minutes=self.duration_minutes),
        ).exclude(pk=self.pk)

        if overlapping_reservations.exists():
            raise ValidationError('Этот столик уже забронирован на указанную дату и время')

    def save(self, *args, **kwargs):
        # Проверка валидации модели перед сохранением
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.customer_name} столик ({self.table_id}) на {self.reservation_time}'
