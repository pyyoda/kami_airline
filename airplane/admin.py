from django.contrib import admin

from .models import Airplane

admin.site.site_header = "Kami Airlines"


# Register your models here.
@admin.register(Airplane)
class AirplaneAdmin(admin.ModelAdmin):
    """Airplane admin class for django admin panel"""

    list_display = (
        "id",
        "airplane_id",
        "passenger_count",
        "fuel_tank_capacity",
        "fuel_consumption_per_minute",
    )
    search_fields = (
        "id",
        "airplane_id",
    )
    list_filter = (
        "id",
        "airplane_id",
        "passenger_count",
    )
    ordering = ["id"]
