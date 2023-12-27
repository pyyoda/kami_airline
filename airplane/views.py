from typing import Any
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Airplane
from .serializers import AirplaneSerializer


class AirplaneViewSet(viewsets.ModelViewSet):
    """Airplane viewset class"""

    queryset = Airplane.objects.all()
    ordering = ["airplane_id"]
    filter_backends = [OrderingFilter, SearchFilter]
    serializer_class = AirplaneSerializer
    model = Airplane
    search_fields = ["id", "airplane_id"]

    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """Creates airplanes and ensures only 10 airplanes are created"""
        if Airplane.objects.count() >= 10:
            return Response(
                {"detail": "Maximum limit of airplanes reached (10)"}, status=400
            )
        return super().create(request, *args, **kwargs)

    @action(
        detail=False,
        methods=["get"],
        url_path="get-fuel-consumption",
        url_name="get_fuel_consumption",
    )
    def get_fuel_consumption(self, request: Request) -> Response:
        """Calculates fuel consumption of all airplanes
        and max minutes to fly for all planes"""
        total_fuel_consumption: float = sum(
            airplane.fuel_consumption_per_minute + (airplane.passenger_count * 0.002)
            for airplane in Airplane.objects.all()
        )

        max_minutes_to_fly: float = min(
            airplane.fuel_tank_capacity / total_fuel_consumption
            for airplane in Airplane.objects.all()
        )

        return Response(
            {
                "Total airplane fuel consumption per minute": total_fuel_consumption,
                "Maximum minutes able to fly": max_minutes_to_fly,
            }
        )
