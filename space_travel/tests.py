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
        self.assertEqual(Pilot.pilot_certification, type(entity_serializer['pilot_certification']))
        self.assertEqual(Pilot.name, type(entity_serializer['name']))
        self.assertEqual(Pilot.age, type(entity_serializer['age']))
        self.assertEqual(Pilot.credits, type(entity_serializer['credits']))
        self.assertEqual(Pilot.location_planet, type(entity_serializer['location_planet']))


class ResourceTestCase(TestCase):
    def setUp(self):
        Resource.objects.create(
            name=resource_name_generate(),
            weight=randint(1, 100)
        )

    def test_fields_persistance(self):
        entity = Resource.objects.all()[0]
        entity_serializer = ResourceSerializer(entity)
        self.assertEqual(Resource.name, type(entity_serializer['name']))
        self.assertEqual(Resource.weight, type(entity_serializer['weight']))


class ContractTestCase(TestCase):
    def setUp(self):
        Contract.objects.create(
            description=description_generate(),
            payload={"resources": [Resource.objects.all()[0]]},
            origin_planet=planet_name_generate(),
            destination_planet=planet_name_generate(),
            value=randint(100, 999999)
        )

    def test_fields_persistance(self):
        entity = Contract.objects.all()[0]
        entity_serializer = ContractSerializer(entity)
        self.assertEqual(Contract.description, type(entity_serializer['description']))
        self.assertEqual(Contract.payload, type(entity_serializer['payload']))
        self.assertEqual(Contract.origin_planet, type(entity_serializer['origin_planet']))
        self.assertEqual(Contract.destination_planet, type(entity_serializer['destination_planet']))
        self.assertEqual(Contract.value, type(entity_serializer['value']))


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
        self.assertEqual(Ship.fuel_capacity, type(entity_serializer['fuel_capacity']))
        self.assertEqual(Ship.fuel_level, type(entity_serializer['fuel_level']))
        self.assertEqual(Ship.weight_capacity, type(entity_serializer['weight_capacity']))
