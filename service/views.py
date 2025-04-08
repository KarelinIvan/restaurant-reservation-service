from rest_framework import generics
from .models import Table, Reservation
from .serializers import TableSerializer, ReservationSerializer
from rest_framework.exceptions import ValidationError


class TableList(generics.ListAPIView):
    """ Отображение всех столиков """
    queryset = Table.objects.all()
    serializer_class = TableSerializer


class TableListCreateView(generics.ListCreateAPIView):
    """ Запись столика """
    queryset = Table.objects.all()
    serializer_class = TableSerializer


class TableDeleteView(generics.DestroyAPIView):
    """ Удаление столика """
    queryset = Table.objects.all()
    serializer_class = TableSerializer


class ReservationList(generics.ListAPIView):
    """ Отображение списка всех бронирований """
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class ReservationListCreateView(generics.ListCreateAPIView):
    """ Запись брони """
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def perform_create(self, serializer):
        try:
            serializer.save()
        except Exception as e:
            raise ValidationError(str(e))


class ReservationDeleteView(generics.DestroyAPIView):
    """ Удаление брони """
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
