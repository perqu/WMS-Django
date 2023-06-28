from rest_framework import serializers
from .models import Warehouse, Zone, Rack, Shelf, ProductStorageLink


class ProductStorageLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductStorageLink
        fields = "__all__"


class ShelfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shelf
        fields = "__all__"


class RackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rack
        fields = "__all__"


class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = "__all__"


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = "__all__"
