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
from rest_framework.test import APIClient


class PilotTestCase(TestCase):
    def test_create_empty(self):
        client = APIClient()
        data = {}
        response = client.post('/pilots', data, format='json')
        self.assertEqual(response.status_code, 400)

class PlanetTestCase(TestCase):
    def test_create_empty(self):
        client = APIClient()
        data = {}
        response = client.post('/planets', data, format='json')
        self.assertEqual(response.status_code, 400)


class TravelTestCase(TestCase):
    def test_create_empty(self):
        client = APIClient()
        data = {}
        response = client.post('/travels', data, format='json')
        self.assertEqual(response.status_code, 400)


class ResourceTestCase(TestCase):
    def test_create_empty(self):
        client = APIClient()
        data = {}
        response = client.post('/resources', data, format='json')
        self.assertEqual(response.status_code, 400)


class ContractTestCase(TestCase):
    def test_create_empty(self):
        client = APIClient()
        data = {}
        response = client.post('/contracts', data, format='json')
        self.assertEqual(response.status_code, 400)


class ShipTestCase(TestCase):
    def test_create_empty(self):
        client = APIClient()
        data = {}
        response = client.post('/ships', data, format='json')
        self.assertEqual(response.status_code, 400)
