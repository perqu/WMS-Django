from rest_framework import generics
from .models import Warehouse, Zone, Rack, Shelf
from .serializers import (
    WarehouseSerializer,
    ZoneSerializer,
    RackSerializer,
    ShelfSerializer,
)
from rest_framework.permissions import IsAuthenticated


### Warehouses ###
class WarehouseListCreateView(generics.ListCreateAPIView):
    """
    Endpoint for creating and listing warehouses.
    """

    permission_classes = [IsAuthenticated]
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer


class WarehouseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Endpoint for retrieving, updating and deleting a warehouse.
    """

    permission_classes = [IsAuthenticated]
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer


### Zones ###
class ZoneListCreateView(generics.ListCreateAPIView):
    """
    Endpoint for creating and listing zone.
    """

    permission_classes = [IsAuthenticated]
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer


class ZoneRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Endpoint for retrieving, updating and deleting a zone.
    """

    permission_classes = [IsAuthenticated]
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer


### Racks ###
class RackListCreateView(generics.ListCreateAPIView):
    """
    Endpoint for creating and listing Rack.
    """

    permission_classes = [IsAuthenticated]
    queryset = Rack.objects.all()
    serializer_class = RackSerializer


class RackRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Endpoint for retrieving, updating and deleting a Rack.
    """

    permission_classes = [IsAuthenticated]
    queryset = Rack.objects.all()
    serializer_class = RackSerializer


### Shelves ###
class ShelfListCreateView(generics.ListCreateAPIView):
    """
    Endpoint for creating and listing Shelf.
    """

    permission_classes = [IsAuthenticated]
    queryset = Shelf.objects.all()
    serializer_class = ShelfSerializer


class ShelfRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Endpoint for retrieving, updating and deleting a Shelf.
    """

    permission_classes = [IsAuthenticated]
    queryset = Shelf.objects.all()
    serializer_class = ShelfSerializer
