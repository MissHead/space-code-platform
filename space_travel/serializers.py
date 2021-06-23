from rest_framework import serializers
from space_travel.models import (
    Pilot,
    Resource,
    Contract,
    Ship
)


class PilotSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pilot
        fields = (
            'id',
            'pilot_certification',
            'name',
            'age',
            'credits',
            'location_planet',
            'created_at',
            'disabled_at'
        )


class ResourceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Resource
        fields = (
            'id',
            'name',
            'weight',
            'created_at',
            'disabled_at'
        )


class ContractSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contract
        fields = (
            'id',
            'description',
            'payload',
            'origin_planet',
            'destination_planet',
            'value',
            'created_at',
            'disabled_at'
        )


class ShipSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ship
        fields = (
            'id',
            'fuel_capacity',
            'fuel_level',
            'weight_capacity',
            'created_at',
            'disabled_at'
        )
