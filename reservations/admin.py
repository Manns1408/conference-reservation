from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Rooms, TheReservation

class ReservationsInline(admin.TabularInline):
    """
    Shows the reservations inline on the Room admin page.
    """
    model = TheReservation
    extra = 0
    fields = ('user', 'start_time', 'end_time', 'created_at')
    readonly_fields = ('created_at',)

@admin.register(Rooms)
class RoomAdmin(admin.ModelAdmin):
    """
    Admin interface for Rooms.
    """
    list_display  = ('name', 'location', 'capacity')
    search_fields = ('name', 'location')
    list_filter   = ('capacity',)
    inlines       = [ReservationsInline]

@admin.register(TheReservation)
class AdminReservation(admin.ModelAdmin):
    """
    Admin interface for Reservations.
    """
    list_display   = ('room', 'user', 'start_time', 'end_time', 'created_at')
    list_filter    = ('room', 'user')
    search_fields  = ('room__name', 'user__username')
    date_hierarchy = 'start_time'

# Allow admin to manage user accounts
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
