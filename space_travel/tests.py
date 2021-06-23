import names
from random import randint
from django.test import TestCase
from space_travel.helpers import (
    certification_generate,
    planet_name_generate,
    resource_name_generate,
    description_generate
)
from space_travel.models import (
    Pilot,
    Resource,
    Contract,
    Ship
)


class PilotTestCase(TestCase):
    def setUp(self):
        Pilot.objects.create(
            {
                "pilot_certification": certification_generate(),
                "name": names.get_full_name(),
                "age": randint(1, 100),
                "credits": randint(100, 999999),
                "location_planet": planet_name_generate(),
            }
        )

class ResourceTestCase(TestCase):
    def setUp(self):
        Resource.objects.create(
            {
                "name": resource_name_generate(),
                "weight": randint(1, 100)
            }
        )


class ContractTestCase(TestCase):
    def setUp(self):
        Contract.objects.create(
            {
                "description": description_generate()
            }
        )

class ShipTestCase(TestCase):
    def setUp(self):
        Ship.objects.create()