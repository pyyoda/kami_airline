from rest_framework import serializers
from .models import Airplane


class AirplaneSerializer(serializers.ModelSerializer):
    """Airplane default serializer class"""
    fuel_tank_capacity: int = serializers.SerializerMethodField()
    fuel_consumption_per_minute: float = serializers.SerializerMethodField()

    class Meta:
        model = Airplane
        fields = [
            "id",
            "airplane_id",
            "passenger_count",
            "fuel_tank_capacity",
            "fuel_consumption_per_minute",
        ]

    def get_fuel_tank_capacity(self, obj: Airplane) -> int:
        """uses property fuel tank capacity"""
        return obj.fuel_tank_capacity

    def get_fuel_consumption_per_minute(self, obj: Airplane) -> float:
        """uses property fuel consumption per minute"""
        return obj.fuel_consumption_per_minute
