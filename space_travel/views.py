import datetime
import subprocess
from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.utils.serializer_helpers import BindingDict

from space_travel.models import (
    Pilot,
    Resource,
    Contract,
    Ship,
    Planet,
    Travel,
    FuelRefill
)
from space_travel.serializers import (
    PilotSerializer,
    ResourceSerializer,
    ContractSerializer,
    ShipSerializer,
    PlanetSerializer,
    TravelSerializer,
    FuelRefillSerializer
)
from rest_framework.decorators import api_view


@api_view(['GET'])
def health_check(request):
    version = subprocess.check_output(["git", "describe", "--always", "--tags"]).strip().decode('utf-8')
    return JsonResponse({"version": version}, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def pilot_controller(request):
    if request.method == 'GET':
        pilots = Pilot.objects.filter(disabled_at=None)
        pilots_serializer = PilotSerializer(pilots, many=True)
        return JsonResponse(pilots_serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        pilot_serializer = PilotSerializer(data=data)
        if pilot_serializer.is_valid():
            pilot_serializer.save()
            return JsonResponse(pilot_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(pilot_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return JsonResponse({'message': 'Method not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET', 'PUT', 'DELETE'])
def pilot_handle(request, _id):
    pilot = Pilot.objects.get(pk=_id)
    pilot_serializer = PilotSerializer(pilot)
    if request.method == 'GET':
        return JsonResponse(pilot_serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        data = pilot_serializer.data
        credits = data['credits']
        request_data = JSONParser().parse(request)
        contract = Contract.objects.filter(pilot=data['id'])
        if contract.count() > 0:
            contract_serializer = ContractSerializer(contract[0])
            if 'location_planet' in request_data:
                travel = Travel.objects.get(pk=contract_serializer.data['travel'])
                travel_serializer = TravelSerializer(travel)
                _from = PlanetSerializer(Planet.objects.get(pk=data['location_planet']))
                _to = PlanetSerializer(Planet.objects.get(pk=request_data['location_planet']))
                for item in travel_serializer.data['route']['map']:
                    destination = '{} to {}'.format(_from.data['name'], _to.data['name'])
                    if destination in item.keys():
                        credits = credits - item[destination]
                        if credits < 0:
                            return JsonResponse({'message': 'Insufficient funds.'}, status=status.HTTP_400_BAD_REQUEST)
                request_data['credits'] = credits
        data.pop('disabled_at', None)
        data.update(request_data)
        pilot_serializer = PilotSerializer(pilot, data)
        if pilot_serializer.is_valid():
            pilot_serializer.save()
            return JsonResponse(pilot_serializer.data, status=status.HTTP_200_OK)
        else:
            return JsonResponse(pilot_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        pilot.delete()
        return JsonResponse({'message': 'deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
    else:
        return JsonResponse({'message': 'Method not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET', 'POST'])
def resource_controller(request):
    if request.method == 'GET':
        resources = Resource.objects.filter(disabled_at=None)
        resources_serializer = ResourceSerializer(resources, many=True)
        return JsonResponse(resources_serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        resource_serializer = ResourceSerializer(data=data)
        if resource_serializer.is_valid():
            resource_serializer.save()
            Resource.objects.create(name=resource_serializer.data['name'], id=resource_serializer.data['id'])
            return JsonResponse(resource_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(resource_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return JsonResponse({'message': 'Method not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET', 'PUT', 'DELETE'])
def resource_handle(request, _id):
    resource = Resource.objects.get(pk=_id)
    resource_serializer = ResourceSerializer(resource)
    if request.method == 'GET':
        return JsonResponse(resource_serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        data = resource_serializer.data
        data.pop('disabled_at', None)
        data.update(JSONParser().parse(request))
        resource_serializer = ResourceSerializer(resource, data)
        if resource_serializer.is_valid():
            resource_serializer.save()
            return JsonResponse(resource_serializer.data, status=status.HTTP_200_OK)
        else:
            return JsonResponse(resource_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        resource.delete()
        return JsonResponse({'message': 'deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
    else:
        return JsonResponse({'message': 'Method not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET', 'POST'])
def contract_controller(request):
    if request.method == 'GET':
        contract = Contract.objects.filter(disabled_at=None)
        contract_serializer = ContractSerializer(contract, many=True)
        return JsonResponse(contract_serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        contract_serializer = ContractSerializer(data=data)
        if contract_serializer.is_valid():
            contract_serializer.save()
            return JsonResponse(contract_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(contract_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return JsonResponse({'message': 'Method not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET', 'PUT', 'DELETE'])
def contract_handle(request, _id):
    contract = Contract.objects.get(pk=_id)
    contract_serializer = ContractSerializer(contract)
    if request.method == 'GET':
        return JsonResponse(contract_serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        data = contract_serializer.data
        request_data = JSONParser().parse(request)
        pilot = contract.pilot
        pilot_data = PilotSerializer(pilot).data
        if 'status' in request_data:
            if request_data['status']:
                credits = pilot.credits + contract.value
                pilot_data.update({'credits': credits})
                pilot_data.pop('disabled_at')
                pilot_serializer = PilotSerializer(pilot, data=pilot_data)
                if pilot_serializer.is_valid():
                    pilot_serializer.save()
                request_data['disabled_at'] = datetime.datetime.now()
        data.update(request_data)
        contract_serializer = ContractSerializer(contract, data)
        if contract_serializer.is_valid():
            contract_serializer.save()
            return JsonResponse(contract_serializer.data, status=status.HTTP_200_OK)
        else:
            return JsonResponse(contract_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        contract.delete()
        return JsonResponse({'message': 'deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
    else:
        return JsonResponse({'message': 'Method not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET', 'POST'])
def ship_controller(request):
    if request.method == 'GET':
        ships = Ship.objects.filter(disabled_at=None)
        ships_serializer = ShipSerializer(ships, many=True)
        return JsonResponse(ships_serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        ship_serializer = ShipSerializer(data=data)
        if ship_serializer.is_valid():
            ship_serializer.save()
            return JsonResponse(ship_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(ship_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return JsonResponse({'message': 'Method not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET', 'PUT', 'DELETE'])
def ship_handle(request, _id):
    ship = Ship.objects.get(pk=_id)
    ship_serializer = ShipSerializer(ship)
    if request.method == 'GET':
        return JsonResponse(ship_serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        data = ship_serializer.data
        data.pop('disabled_at', None)
        data.update(JSONParser().parse(request))
        ship_serializer = ShipSerializer(ship, data)
        if ship_serializer.is_valid():
            ship_serializer.save()
            return JsonResponse(ship_serializer.data, status=status.HTTP_200_OK)
        else:
            return JsonResponse(ship_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        ship.delete()
        return JsonResponse({'message': 'deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
    else:
        return JsonResponse({'message': 'Method not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET', 'POST'])
def planet_controller(request):
    if request.method == 'GET':
        planets = Planet.objects.filter(disabled_at=None)
        planets_serializer = PlanetSerializer(planets, many=True)
        return JsonResponse(planets_serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        planet_serializer = PlanetSerializer(data=data)
        if planet_serializer.is_valid():
            planet_serializer.save()
            Planet.objects.create(name=planet_serializer.data['name'], id=planet_serializer.data['id'])
            return JsonResponse(planet_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(planet_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return JsonResponse({'message': 'Method not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET', 'PUT', 'DELETE'])
def planet_handle(request, _id):
    planet = Planet.objects.get(pk=_id)
    planet_serializer = PlanetSerializer(planet)
    if request.method == 'GET':
        return JsonResponse(planet_serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        data = planet_serializer.data
        data.pop('disabled_at', None)
        data.update(JSONParser().parse(request))
        planet_serializer = PlanetSerializer(planet, data)
        if planet_serializer.is_valid():
            planet_serializer.save()
            return JsonResponse(planet_serializer.data, status=status.HTTP_200_OK)
        else:
            return JsonResponse(planet_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        planet.delete()
        return JsonResponse({'message': 'deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
    else:
        return JsonResponse({'message': 'Method not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET', 'POST'])
def travel_controller(request):
    if request.method == 'GET':
        travels = Travel.objects.filter(disabled_at=None)
        travels_serializer = TravelSerializer(travels, many=True)
        return JsonResponse(travels_serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        travel_serializer = TravelSerializer(data=data)
        if travel_serializer.is_valid():
            travel_serializer.save()
            return JsonResponse(travel_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(travel_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return JsonResponse({'message': 'Method not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET', 'PUT', 'DELETE'])
def travel_handle(request, _id):
    travel = Travel.objects.get(pk=_id)
    travel_serializer = TravelSerializer(travel)
    if request.method == 'GET':
        return JsonResponse(travel_serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        data = travel_serializer.data
        data.pop('disabled_at', None)
        data.update(JSONParser().parse(request))
        travel_serializer = TravelSerializer(travel, data)
        if travel_serializer.is_valid():
            travel_serializer.save()
            return JsonResponse(travel_serializer.data, status=status.HTTP_200_OK)
        else:
            return JsonResponse(travel_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        travel.delete()
        return JsonResponse({'message': 'deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
    else:
        return JsonResponse({'message': 'Method not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET', 'POST'])
def fuel_refill_controller(request):
    if request.method == 'GET':
        fuel_refills = FuelRefill.objects.filter(disabled_at=None)
        fuel_refills_serializer = FuelRefillSerializer(fuel_refills, many=True)
        return JsonResponse(fuel_refills_serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        fuel_refill_serializer = FuelRefillSerializer(data=data)
        if fuel_refill_serializer.is_valid():
            pilot = Pilot.objects.get(pk=data['pilot'])
            pilot_data = PilotSerializer(pilot).data
            ship = Ship.objects.get(pilot=data['pilot'])
            ship_data = ShipSerializer(ship).data
            total_fuel = ship.fuel_level + data['value']/700
            credits = pilot.credits - data['value']
            if total_fuel <= ship.fuel_capacity:
                if credits > 0:
                    pilot_data.update({'credits': credits})
                    pilot_data.pop('disabled_at')
                    pilot_serializer = PilotSerializer(pilot, data=pilot_data)
                    if pilot_serializer.is_valid():
                        pilot_serializer.save()
                else:
                    return JsonResponse({'message': 'Insufficient funds.'}, status=status.HTTP_400_BAD_REQUEST)
                ship_data.update({'fuel_level': int(total_fuel)})
                ship_data.pop('disabled_at')
                ship_serializer = ShipSerializer(ship, data=ship_data)
                if ship_serializer.is_valid():
                    ship_serializer.save()
            else:
                return JsonResponse({'message': 'Fuel capacity limit exceeded.'}, status=status.HTTP_400_BAD_REQUEST)
            fuel_refill_serializer.save()
            return JsonResponse(fuel_refill_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(fuel_refill_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return JsonResponse({'message': 'Method not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET', 'PUT', 'DELETE'])
def fuel_refill_handle(request, _id):
    fuel_refill = FuelRefill.objects.get(pk=_id)
    fuel_refill_serializer = FuelRefillSerializer(fuel_refill)
    if request.method == 'GET':
        return JsonResponse(fuel_refill_serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        data = fuel_refill_serializer.data
        data.pop('disabled_at', None)
        data.update(JSONParser().parse(request))
        fuel_refill_serializer = FuelRefillSerializer(fuel_refill, data)
        if fuel_refill_serializer.is_valid():
            fuel_refill_serializer.save()
            return JsonResponse(fuel_refill_serializer.data, status=status.HTTP_200_OK)
        else:
            return JsonResponse(fuel_refill_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        fuel_refill.delete()
        return JsonResponse({'message': 'deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    else:
        return JsonResponse({'message': 'Method not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
