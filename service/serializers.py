from django.utils import timezone
from rest_framework import serializers

from service.models import Table, Reservation


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

    def validate_reservation_time(self, value):
        """ Валидация даты бронирования """
        if value < timezone.now():
            raise serializers.ValidationError('Нельзя бронировать столик на прошедшее время')
        return value
