from django.db.utils import IntegrityError
from django.test import TestCase

from .tests_models import AirplaneFactory


class TestAirplaneViewSet(TestCase):
    def test_unique_airplane_creation(self):
        """Tests uniqueness of airplane ids"""
        with self.assertRaises(IntegrityError):
            airplane_1 = AirplaneFactory()
            AirplaneFactory(airplane_id=airplane_1.airplane_id)
