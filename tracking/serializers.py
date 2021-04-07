from rest_framework import serializers
from .models import Ship, Position


class ShipSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Ship
        fields = ['imo_number', 'name']

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ['timestamp', 'latitude', 'longitude']

class ShipPositionSerializer(serializers.HyperlinkedModelSerializer):
    position_set = PositionSerializer(many=True)

    class Meta:
        model = Ship
        fields = ['imo_number', 'name', "position_set"]
    
