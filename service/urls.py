from django.contrib import admin
from django.urls import path
from service.views import (
    TableListCreateView,
    TableDeleteView,
    ReservationListCreateView,
    ReservationDeleteView, TableList, ReservationList
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tables/', TableList.as_view(), name='table-list'),
    path('table/', TableListCreateView.as_view(), name='table-create'),
    path('tables/<int:pk>/', TableDeleteView.as_view(), name='table-delete'),
    path('reservations/', ReservationList.as_view(), name='reservation-list'),
    path('reservation/', ReservationListCreateView.as_view(), name='reservation-create'),
    path('reservations/<int:pk>/', ReservationDeleteView.as_view(), name='reservation-delete'),
]
