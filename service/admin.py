from django.contrib import admin

from service.models import Table, Reservation


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'seats', 'location')
    search_fields = ('name',)


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'table_id', 'reservation_time', 'duration_minutes')
    search_fields = ('customer_name',)
