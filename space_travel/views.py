import datetime
import subprocess
from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

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
from rest_framework.decorators import api_view


@api_view(['GET'])
def health_check(request):
    version = subprocess.check_output(["git", "describe", "--always", "--tags"]).strip().decode('utf-8')
    return JsonResponse({"version": version}, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def pilot_controller(request):
    if request.method == 'GET':
        pilots = Pilot.objects.all()
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
    if not pilot:
        return JsonResponse({'message': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        pilot_serializer = PilotSerializer(pilot)
        return JsonResponse(pilot_serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        pilot_serializer = PilotSerializer(pilot, data=data)
        if pilot_serializer.is_valid():
            pilot_serializer.save()
            return JsonResponse(pilot_serializer.data, status=status.HTTP_200_OK)
        else:
            return JsonResponse(pilot_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        pilot_serializer = PilotSerializer(pilot, data={'disabled_at': datetime.datetime.now()})
        pilot_serializer.save()
        return JsonResponse({}, status=status.HTTP_204_NO_CONTENT)
    else:
        return JsonResponse({'message': 'Method not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET', 'POST'])
def resource_controller(request):
    if request.method == 'GET':
        resources = Resource.objects.all()
        resources_serializer = ResourceSerializer(resources, many=True)
        return JsonResponse(resources_serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        resource_serializer = ResourceSerializer(data=data)
        if resource_serializer.is_valid():
            resource_serializer.save()
            return JsonResponse(resource_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(resource_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return JsonResponse({'message': 'Method not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET', 'PUT', 'DELETE'])
def resource_handle(request, _id):
    resource = Resource.objects.get(pk=_id)
    if not resource:
        return JsonResponse({'message': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        resource_serializer = ResourceSerializer(resource)
        return JsonResponse(resource_serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        resource_serializer = ResourceSerializer(resource, data=data)
        if resource_serializer.is_valid():
            resource_serializer.save()
            return JsonResponse(resource_serializer.data, status=status.HTTP_200_OK)
        else:
            return JsonResponse(resource_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        resource_serializer = ResourceSerializer(resource, data={'disabled_at': datetime.datetime.now()})
        resource_serializer.save()
        return JsonResponse({}, status=status.HTTP_204_NO_CONTENT)
    else:
        return JsonResponse({'message': 'Method not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET', 'POST'])
def contract_controller(request):
    if request.method == 'GET':
        contract = Contract.objects.all()
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
    if not contract:
        return JsonResponse({'message': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        contracts_serializer = ContractSerializer(contract)
        return JsonResponse(contracts_serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        contract_serializer = ContractSerializer(contract, data=data)
        if contract_serializer.is_valid():
            contract_serializer.save()
            return JsonResponse(contract_serializer.data, status=status.HTTP_200_OK)
        else:
            return JsonResponse(contract_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        contract_serializer = ContractSerializer(contract, data={'disabled_at': datetime.datetime.now()})
        contract_serializer.save()
        return JsonResponse({}, status=status.HTTP_204_NO_CONTENT)
    else:
        return JsonResponse({'message': 'Method not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET', 'POST'])
def ship_controller(request):
    if request.method == 'GET':
        ships = Ship.objects.all()
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
    if not ship:
        return JsonResponse({'message': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        ship_serializer = ShipSerializer(ship)
        return JsonResponse(ship_serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        ship_serializer = ShipSerializer(ship, data=data)
        if ship_serializer.is_valid():
            ship_serializer.save()
            return JsonResponse(ship_serializer.data, status=status.HTTP_200_OK)
        else:
            return JsonResponse(ship_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        ship_serializer = ShipSerializer(ship, data={'disabled_at': datetime.datetime.now()})
        ship_serializer.save()
        return JsonResponse({}, status=status.HTTP_204_NO_CONTENT)
    else:
        return JsonResponse({'message': 'Method not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
