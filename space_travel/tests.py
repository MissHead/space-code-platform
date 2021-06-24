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
    Ship,
    Planet,
    Travel
)
from space_travel.serializers import (
    PilotSerializer,
    ResourceSerializer,
    ContractSerializer,
    ShipSerializer,
    PlanetSerializer,
    TravelSerializer
)


class PilotTestCase(TestCase):
    def setUp(self):
        Pilot.objects.create(
            pilot_certification=certification_generate(),
            name=names.get_full_name(),
            age=randint(1, 100),
            credits=randint(100, 999999),
            location_planet=1
        )


class PlanetTestCase(TestCase):
    def setUp(self):
        Planet.objects.create(
            name=resource_name_generate(),
        )


class TravelTestCase(TestCase):
    def setUp(self):
        Travel.objects.create(
            origin_planet=1,
            destination_planet=2,
            route={(1,5): 32, (5,2):12},
            fuel_costs=44
        )


class ResourceTestCase(TestCase):
    def setUp(self):
        Resource.objects.create(
            name=resource_name_generate(),
            weight=randint(1, 100)
        )


class ContractTestCase(TestCase):
    def setUp(self):
        Contract.objects.create(
            description=description_generate(),
            payload={
                "resources": 
                    [
                        {"name": resource_name_generate(), "weight": randint(1, 100)},
                        {"name": resource_name_generate(), "weight": randint(1, 100)}
                    ]
                },
            origin_planet=planet_name_generate(),
            destination_planet=planet_name_generate(),
            value=randint(100, 999999)
        )


class ShipTestCase(TestCase):
    def setUp(self):
        Ship.objects.create(
            fuel_capacity=randint(1, 100),
            fuel_level=randint(1, 100),
            weight_capacity=randint(1, 100)
        )
