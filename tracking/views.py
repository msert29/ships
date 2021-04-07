from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework import generics

from .models import Ship, Position
from .serializers import ShipSerializer, ShipPositionSerializer

class ShipView(generics.ListAPIView):
    """
    API endpoint that displays a list of ships containing IMO and ship name.
    /api/ships/
    """
    queryset = Ship.objects.all()
    serializer_class = ShipSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

class PositionView(generics.RetrieveAPIView):
    """
    API endpoint that displays positions of a given by latitude, longitude and timestamp in decending order by timestamp.
    /api/positions/<int:imo_number>/
    """
    queryset = Ship.objects.all()
    serializer_class = ShipPositionSerializer

    def get(self, request, *args, **kwargs):
        imo_number = kwargs.get("imo_number")
        ship = get_object_or_404(Ship, imo_number=imo_number)
        serializer = self.serializer_class(ship)
        return Response(serializer.data)

def index(request):
    return render(request, "index.html")