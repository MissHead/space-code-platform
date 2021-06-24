from rest_framework import serializers
from space_travel.models import (
    Pilot,
    Resource,
    Contract,
    Ship,
    Planet,
    Travel
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

    def validate_pilot_certification(self, data):
        certification = [int(char) for char in data if char.isdigit()]
        if len(certification) != 7:
            return False
        if certification == certification[::-1]:
            return False
        value = sum((certification[num] * ((6+1) - num) for num in range(0, 6)))
        digit = ((value * 10) % 7) % 10
        if digit != certification[6]:
            raise serializers.ValidationError("Invalid certification.")
        return data

    def validate_location_planet(self, data):
        try:
            p = Planet.objects.get(pk=data)
        except Exception:
            raise serializers.ValidationError("Invalid planet id.")
        return data


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

    def validate_payload(self, data):
        if 'resources' not in data.keys():
            raise serializers.ValidationError("Invalid payload key.")
        for _id in data['resources']:
            try:
                r = Resource.objects.get(pk=_id)
            except Exception:
                raise serializers.ValidationError("Invalid resource id.")
        return data

    def validate_origin_planet(self, data):
        try:
            p = Planet.objects.get(pk=data)
        except Exception:
            raise serializers.ValidationError("Invalid planet id.")
        return data

    def validate_destination_planet(self, data):
        try:
            p = Planet.objects.get(pk=data)
        except Exception:
            raise serializers.ValidationError("Invalid planet id.")
        return data


class ShipSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ship
        fields = (
            'id',
            'fuel_capacity',
            'fuel_level',
            'weight_capacity',
            'pilot'
        )

    def validate_pilot(self, data):
        try:
            p = Pilot.objects.get(pk=data)
        except Exception:
            raise serializers.ValidationError("Invalid pilot id.")
        return data


class PlanetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Planet
        fields = (
            'id',
            'name'
        )


class TravelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Travel
        fields = (
            'origin_planet',
            'destination_planet',
            'route',
            'fuel_costs',
            'created_at',
            'disabled_at'
        )

    def validate_origin_planet(self, data):
        try:
            p = Planet.objects.get(pk=data)
        except Exception:
            raise serializers.ValidationError("Invalid planet id.")
        return data

    def validate_destination_planet(self, data):
        try:
            p = Planet.objects.get(pk=data)
        except Exception:
            raise serializers.ValidationError("Invalid planet id.")
        return data