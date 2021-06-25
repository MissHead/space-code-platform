import names
from random import randint
import names
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
from rest_framework.test import APIClient


class PilotTestCase(TestCase):
    def test_create_empty(self):
        client = APIClient()
        data = {}
        response = client.post('/pilots', data, format='json')
        self.assertEqual(response.status_code, 400)
    def test_create(self):
        client = APIClient()
        planet = Planet.objects.create(name=planet_name_generate())
        data = {
            "name": names.get_full_name(),
            "age": randint(1, 99),
            "pilot_certification": certification_generate(),
            "location_planet": planet.id
        }
        response = client.post('/pilots', data, format='json')
        self.assertEqual(response.status_code, 201)
    def test_update(self):
        client = APIClient()
        planet = Planet.objects.create(name=planet_name_generate())
        pilot = Pilot.objects.create(name=names.get_full_name(), age=randint(1, 99), pilot_certification=certification_generate(), location_planet=planet)
        data = {
            "age": randint(1, 99)
        }
        response = client.put('/pilot/{}'.format(pilot.id), data, format='json')
        self.assertEqual(response.status_code, 200)
    def test_show(self):
        client = APIClient()
        planet = Planet.objects.create(name=planet_name_generate())
        pilot = Pilot.objects.create(name=names.get_full_name(), age=randint(1, 99), pilot_certification=certification_generate(), location_planet=planet)
        response = client.get('/pilot/{}'.format(pilot.id), format='json')
        self.assertEqual(response.status_code, 200)
    def test_delete(self):
        client = APIClient()
        planet = Planet.objects.create(name=planet_name_generate())
        pilot = Pilot.objects.create(name=names.get_full_name(), age=randint(1, 99), pilot_certification=certification_generate(), location_planet=planet)
        response = client.delete('/pilot/{}'.format(pilot.id), format='json')
        self.assertEqual(response.status_code, 204)


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
