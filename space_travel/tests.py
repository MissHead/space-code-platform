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
    Travel,
    FuelRefill
)
from rest_framework.test import APIClient


def generate_pilot():
    planet = Planet.objects.create(name=planet_name_generate())
    pilot = Pilot.objects.create(name=names.get_full_name(), age=randint(1, 99), pilot_certification=certification_generate(), location_planet=planet, credits=randint(1000, 999999))
    ship = Ship.objects.create(
            fuel_capacity=randint(50, 99),
            fuel_level=randint(50, 99),
            weight_capacity=randint(1, 50),
            pilot=pilot
        )
    return pilot

def generate_planet():
    return Planet.objects.create(name=planet_name_generate())

def generate_resource():
    return Resource.objects.create(name=resource_name_generate(), weight=randint(1, 100))

def generate_travel():
    origin_planet = Planet.objects.create(name=planet_name_generate())
    destination_planet = Planet.objects.create(name=planet_name_generate())
    cost_origin_to_destination = randint(1, 50) * 100
    return Travel.objects.create(
        origin_planet=origin_planet,
        destination_planet=destination_planet,
        route={"map": [{"{} to {}".format(origin_planet.name, destination_planet.name): cost_origin_to_destination}]},
        fuel_costs=cost_origin_to_destination
    )

def generate_ship():
    planet = Planet.objects.create(name=planet_name_generate())
    pilot = Pilot.objects.create(name=names.get_full_name(), age=randint(1, 99), pilot_certification=certification_generate(), location_planet=planet)
    return Ship.objects.create(
            fuel_capacity=randint(50, 99),
            fuel_level=randint(50, 99),
            weight_capacity=randint(1, 50),
            pilot=pilot
        )

def generate_fuel_refill():
    planet = Planet.objects.create(name=planet_name_generate())
    pilot = Pilot.objects.create(name=names.get_full_name(), age=randint(1, 99), pilot_certification=certification_generate(), location_planet=planet)
    return FuelRefill.objects.create(
        pilot=pilot,
        value=randint(100, 1000),
        location_planet=planet
    )

def generate_contract():
    resource = Resource.objects.create(name=resource_name_generate(), weight=randint(1, 100))
    planet = Planet.objects.create(name=planet_name_generate())
    pilot = Pilot.objects.create(name=names.get_full_name(), age=randint(1, 99), pilot_certification=certification_generate(), location_planet=planet)
    origin_planet = Planet.objects.create(name=planet_name_generate())
    destination_planet = Planet.objects.create(name=planet_name_generate())
    cost_origin_to_destination = randint(1, 50) * 100
    travel = Travel.objects.create(
        origin_planet=origin_planet,
        destination_planet=destination_planet,
        route={"map": [{"{} to {}".format(origin_planet.name, destination_planet.name): cost_origin_to_destination}]},
        fuel_costs=cost_origin_to_destination
    )
    return Contract.objects.create(
        description=description_generate(),
        payload={"resources": [resource.id]},
        origin_planet=origin_planet,
        destination_planet=destination_planet,
        value=randint(100, 999999),
        pilot=pilot,
        travel=travel
    )


class PilotTestCase(TestCase):

    def test_create_empty(self):
        client = APIClient()
        data = {}
        response = client.post('/pilots', data, format='json')
        self.assertEqual(response.status_code, 400)

    def test_create(self):
        client = APIClient()
        planet = generate_planet()
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
        pilot = generate_pilot()
        data = {
            "age": randint(1, 99)
        }
        response = client.put('/pilot/{}'.format(pilot.id), data, format='json')
        self.assertEqual(response.status_code, 200)

    def test_show(self):
        client = APIClient()
        pilot = generate_pilot()
        response = client.get('/pilot/{}'.format(pilot.id), format='json')
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        client = APIClient()
        pilot = generate_pilot()
        response = client.delete('/pilot/{}'.format(pilot.id), format='json')
        self.assertEqual(response.status_code, 204)


class PlanetTestCase(TestCase):

    def test_create_empty(self):
        client = APIClient()
        data = {}
        response = client.post('/planets', data, format='json')
        self.assertEqual(response.status_code, 400)

    def test_create(self):
        client = APIClient()
        data = {
            "name": planet_name_generate(),
        }
        response = client.post('/planets', data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_update(self):
        client = APIClient()
        planet = generate_planet()
        data = {
            "name": planet_name_generate(),
        }
        response = client.put('/planet/{}'.format(planet.id), data, format='json')
        self.assertEqual(response.status_code, 200)

    def test_show(self):
        client = APIClient()
        planet = generate_planet()
        response = client.get('/planet/{}'.format(planet.id), format='json')
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        client = APIClient()
        planet = generate_planet()
        response = client.delete('/planet/{}'.format(planet.id), format='json')
        self.assertEqual(response.status_code, 204)


class TravelTestCase(TestCase):

    def test_create_empty(self):
        client = APIClient()
        data = {}
        response = client.post('/travels', data, format='json')
        self.assertEqual(response.status_code, 400)

    def test_create(self):
        client = APIClient()
        origin_planet = generate_planet()
        destination_planet = generate_planet()
        cost = randint(1, 50) * 100
        data = {
            "origin_planet": origin_planet.id,
            "destination_planet": destination_planet.id,
            "route": {"map": [{"{} to {}".format(origin_planet.name, destination_planet.name): cost}]},
            "fuel_costs": cost
        }
        response = client.post('/travels', data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_update(self):
        client = APIClient()
        planet = generate_planet()
        origin_planet = generate_planet()
        destination_planet = generate_planet()
        cost_origin_to_planet = randint(1, 50) * 100
        cost_planet_to_destination = randint(1, 50) * 100
        travel = generate_travel()
        data = {
            "route": {"map": [
                {"{} to {}".format(origin_planet.name, planet.name): cost_origin_to_planet},
                {"{} to {}".format(planet.name, destination_planet.name): cost_planet_to_destination},
                ]},
            "fuel_costs": (cost_origin_to_planet + cost_planet_to_destination)
        }
        response = client.put('/travel/{}'.format(travel.id), data, format='json')
        self.assertEqual(response.status_code, 200)

    def test_show(self):
        client = APIClient()
        travel = generate_travel()
        response = client.get('/travel/{}'.format(travel.id), format='json')
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        client = APIClient()
        travel = generate_travel()
        response = client.delete('/travel/{}'.format(travel.id), format='json')
        self.assertEqual(response.status_code, 204)


class ResourceTestCase(TestCase):

    def test_create_empty(self):
        client = APIClient()
        data = {}
        response = client.post('/resources', data, format='json')
        self.assertEqual(response.status_code, 400)

    def test_create(self):
        client = APIClient()
        data = {
            "name": resource_name_generate(),
            "weight": randint(1, 100)
        }
        response = client.post('/resources', data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_update(self):
        client = APIClient()
        resource = generate_resource()
        data = {
            "name": resource_name_generate(),
        }
        response = client.put('/resource/{}'.format(resource.id), data, format='json')
        self.assertEqual(response.status_code, 200)

    def test_show(self):
        client = APIClient()
        resource = generate_resource()
        response = client.get('/resource/{}'.format(resource.id), format='json')
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        client = APIClient()
        resource = generate_resource()
        response = client.delete('/resource/{}'.format(resource.id), format='json')
        self.assertEqual(response.status_code, 204)


class ContractTestCase(TestCase):

    def test_create_empty(self):
        client = APIClient()
        data = {}
        response = client.post('/contracts', data, format='json')
        self.assertEqual(response.status_code, 400)

    def test_create(self):
        client = APIClient()
        resource = generate_resource()
        pilot = generate_pilot()
        origin_planet = generate_planet()
        destination_planet = generate_planet()
        travel = generate_travel()
        data = {
            "description": description_generate(),
            "payload": {"resources": [resource.id]},
            "origin_planet": origin_planet.id,
            "destination_planet": destination_planet.id,
            "value": randint(100, 999999),
            "pilot": pilot.id,
            "travel": travel.id
        }
        response = client.post('/contracts', data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_update(self):
        client = APIClient()
        contract = generate_contract()
        data = {
            "value": randint(100, 999999),
        }
        response = client.put('/contract/{}'.format(contract.id), data, format='json')
        self.assertEqual(response.status_code, 200)

    def test_show(self):
        client = APIClient()
        contract = generate_contract()
        response = client.get('/contract/{}'.format(contract.id), format='json')
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        client = APIClient()
        contract = generate_contract()
        response = client.delete('/contract/{}'.format(contract.id), format='json')
        self.assertEqual(response.status_code, 204)


class ShipTestCase(TestCase):
    def test_create_empty(self):
        client = APIClient()
        data = {}
        response = client.post('/ships', data, format='json')
        self.assertEqual(response.status_code, 400)
    def test_create(self):
        client = APIClient()
        pilot = generate_pilot()
        data = {
            "fuel_capacity": randint(50, 99),
            "fuel_level": randint(1, 50),
            "weight_capacity": randint(1, 50),
            "pilot": pilot.id
        }
        response = client.post('/ships', data, format='json')
        self.assertEqual(response.status_code, 201)
    def test_update(self):
        client = APIClient()
        ship = generate_ship()
        data = {
            "fuel_level": randint(50, 99),
        }
        response = client.put('/ship/{}'.format(ship.id), data, format='json')
        self.assertEqual(response.status_code, 200)
    def test_show(self):
        client = APIClient()
        ship = generate_ship()
        response = client.get('/ship/{}'.format(ship.id), format='json')
        self.assertEqual(response.status_code, 200)
    def test_delete(self):
        client = APIClient()
        ship = generate_ship()
        response = client.delete('/ship/{}'.format(ship.id), format='json')
        self.assertEqual(response.status_code, 204)


class FuelRefillTestCase(TestCase):
    def test_create_empty(self):
        client = APIClient()
        data = {}
        response = client.post('/fuel_refills', data, format='json')
        self.assertEqual(response.status_code, 400)
    def test_create(self):
        client = APIClient()
        pilot = generate_pilot()
        planet = generate_planet()
        data = {
            "location_planet": planet.id,
            "value": randint(100, 1000),
            "pilot": pilot.id
        }
        response = client.post('/fuel_refills', data, format='json')
        self.assertEqual(response.status_code, 201)
    def test_update(self):
        client = APIClient()
        fuel_refill = generate_fuel_refill()
        data = {
            "fuel_level": randint(50, 99),
        }
        response = client.put('/fuel_refill/{}'.format(fuel_refill.id), data, format='json')
        self.assertEqual(response.status_code, 200)
    def test_show(self):
        client = APIClient()
        fuel_refill = generate_fuel_refill()
        response = client.get('/fuel_refill/{}'.format(fuel_refill.id), format='json')
        self.assertEqual(response.status_code, 200)
    def test_delete(self):
        client = APIClient()
        fuel_refill = generate_fuel_refill()
        response = client.delete('/fuel_refill/{}'.format(fuel_refill.id), format='json')
        self.assertEqual(response.status_code, 204)


class ReportsTestCase(TestCase):
    def test_get_reports(self):
        client = APIClient()
        generate_fuel_refill().delete()

        generate_fuel_refill().delete()
        generate_contract().delete()
        generate_contract().delete()
        generate_contract().delete()
        generate_contract().delete()
        generate_fuel_refill().delete()
        generate_fuel_refill().delete()
        generate_fuel_refill().delete()
        generate_contract().delete()
        data = {}
        response = client.get('/report/resource_weight', data, format='json')
        self.assertEqual(response.status_code, 200)
        response = client.get('/report/resource_percentage', data, format='json')
        self.assertEqual(response.status_code, 200)
        response = client.get('/report/transactions', data, format='json')
        self.assertEqual(response.status_code, 200)
