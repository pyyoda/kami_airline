from django.db import models
import math


class Airplane(models.Model):
    "Airplane model class"
    airplane_id: int = models.IntegerField(unique=True)
    passenger_count: int = models.IntegerField()

    @property
    def fuel_tank_capacity(self) -> int:
        """Calculate fuel tank capacity based on airplane ID"""
        return self.airplane_id * 200

    @property
    def fuel_consumption_per_minute(self) -> float:
        """Calculate fuel consumption per minute based on the log of airplane ID"""
        return math.log(self.airplane_id) * 0.80

    def __str__(self) -> str:
        """Displays airplane id and it's fuel tank capacity"""
        return f"""Airplane ID: {self.airplane_id},
    Fuel Tank Capacity: {self.fuel_tank_capacity} liters"""

    class Meta:
        verbose_name: str = "Airplane"
        verbose_name_plural: str = "Airplanes"
