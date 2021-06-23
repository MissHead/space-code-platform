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
from space_travel.serializers import (
    PilotSerializer,
    ResourceSerializer,
    ContractSerializer,
    ShipSerializer
)


class PilotTestCase(TestCase):
    def setUp(self):
        Pilot.objects.create(
            pilot_certification=certification_generate(),
            name=names.get_full_name(),
            age=randint(1, 100),
            credits=randint(100, 999999),
            location_planet=planet_name_generate()
        )

    def test_fields_persistance(self):
        entity = Pilot.objects.all()[0]
        entity_serializer = PilotSerializer(entity)
        self.assertEqual(str, type(entity_serializer.data['pilot_certification']))
        self.assertEqual(str, type(entity_serializer.data['name']))
        self.assertEqual(int, type(entity_serializer.data['age']))
        self.assertEqual(int, type(entity_serializer.data['credits']))
        self.assertEqual(str, type(entity_serializer.data['location_planet']))


class ResourceTestCase(TestCase):
    def setUp(self):
        Resource.objects.create(
            name=resource_name_generate(),
            weight=randint(1, 100)
        )

    def test_fields_persistance(self):
        entity = Resource.objects.all()[0]
        entity_serializer = ResourceSerializer(entity)
        self.assertEqual(str, type(entity_serializer.data['name']))
        self.assertEqual(int, type(entity_serializer.data['weight']))


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

    def test_fields_persistance(self):
        entity = Contract.objects.all()[0]
        entity_serializer = ContractSerializer(entity)
        self.assertEqual(str, type(entity_serializer.data['description']))
        self.assertEqual(dict, type(entity_serializer.data['payload']))
        self.assertEqual(str, type(entity_serializer.data['origin_planet']))
        self.assertEqual(str, type(entity_serializer.data['destination_planet']))
        self.assertEqual(int, type(entity_serializer.data['value']))


class ShipTestCase(TestCase):
    def setUp(self):
        Ship.objects.create(
            fuel_capacity=randint(1, 100),
            fuel_level=randint(1, 100),
            weight_capacity=randint(1, 100)
        )

    def test_fields_persistance(self):
        entity = Ship.objects.all()[0]
        entity_serializer = ShipSerializer(entity)
        self.assertEqual(int, type(entity_serializer.data['fuel_capacity']))
        self.assertEqual(int, type(entity_serializer.data['fuel_level']))
        self.assertEqual(int, type(entity_serializer.data['weight_capacity']))
