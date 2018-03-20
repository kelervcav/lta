from rest_framework import serializers
from reviews.models import Review
from management.models import (
    Location, Device, Type, TypeGroup
)


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'name', 'is_active',
                  'is_deleted')


class TypeGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeGroup
        fields = ('id', 'name', 'is_active',
                  'is_deleted')


class TypeSerializer(serializers.ModelSerializer):
    typegroup = TypeGroupSerializer()

    class Meta:
        model = Type
        fields = ('id', 'typegroup', 'name', 'is_active',
                  'is_deleted')


class DeviceSerializer(serializers.ModelSerializer):
    type = TypeSerializer()

    class Meta:
        model = Device
        fields = ('id', 'type', 'name', 'is_active',
                  'is_deleted')


class ReviewSerializer(serializers.ModelSerializer):
    type = TypeSerializer()
    location = LocationSerializer()
    device = DeviceSerializer()

    class Meta:
        model = Review
        fields = ('id', 'type', 'device', 'location', 'date', 'time',
                  'is_active', 'is_deleted', 'speed_limit', 'wrong_path',
                  'rider_dismount', 'weaving', 'no_light', 'no_light',
                  'near_misses',)
