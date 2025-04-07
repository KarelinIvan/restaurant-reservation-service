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
    location = models.CharField(max_length=2, choices=Location.choices ,verbose_name='Расположение столика')

    class Meta:
        verbose_name = 'Столик'
        verbose_name_plural = 'Столики'
        ordering = ['name',]

    def __str__(self):
        return f'{self.name} ({self.seats} seats) - {self.location}'
