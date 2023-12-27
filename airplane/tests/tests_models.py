import math

from django.test import TestCase
from factory.django import DjangoModelFactory
from faker import Faker

from ..models import Airplane


class AirplaneFactory(DjangoModelFactory):
    class Meta:
        model = Airplane

    airplane_id = Faker().unique.random_int()
    passenger_count = Faker().random_int(min=0, max=500)


class TestAirplaneModel(TestCase):
    def test_airplane_creation(self):
        """Tests airplane model properties"""
        # Create an airplane object using factory Airplane model
        airplane = AirplaneFactory()

        # Affirm that the airplane object is an instance of the Airplane model
        self.assertIsInstance(airplane, Airplane)

        # Affirm that the calculated fuel tank capacity matches the expected value
        expected_capacity = airplane.airplane_id * 200
        self.assertEqual(airplane.fuel_tank_capacity, expected_capacity)

        # Affirm that the calculated fuel consumption per minute matches the expected value
        expected_consumption = math.log(airplane.airplane_id) * 0.80
        self.assertEqual(airplane.fuel_consumption_per_minute, expected_consumption)
