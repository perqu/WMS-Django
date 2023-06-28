from django.test import TestCase
from products.models import Product
from ..models import Warehouse, Zone, Rack, Shelf, ProductStorageLink
from ..serializers import (
    ProductStorageLinkSerializer,
    ShelfSerializer,
    RackSerializer,
    ZoneSerializer,
    WarehouseSerializer,
)


class ProductStorageLinkSerializerTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name="Test Product", price=9.99)
        self.warehouse = Warehouse.objects.create(name="Test Warehouse")
        self.zone = Zone.objects.create(name="Test Zone", warehouse=self.warehouse)
        self.rack = Rack.objects.create(name="Test Rack", zone=self.zone)
        self.shelf = Shelf.objects.create(name="Test Shelf", rack=self.rack)
        self.serializer = ProductStorageLinkSerializer(
            instance=ProductStorageLink(
                product_id=self.product, shelf_id=self.shelf, quantity=10
            )
        )

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), {"id", "product", "shelf", "quantity"})

    def test_product_id_field_content(self):
        data = self.serializer.data
        self.assertEqual(data["product"], self.product.id)

    def test_shelf_id_field_content(self):
        data = self.serializer.data
        self.assertEqual(data["shelf"], self.shelf.id)

    def test_quantity_field_content(self):
        data = self.serializer.data
        self.assertEqual(data["quantity"], 10)


class ShelfSerializerTest(TestCase):
    def setUp(self):
        self.warehouse = Warehouse.objects.create(name="Test Warehouse")
        self.zone = Zone.objects.create(name="Test Zone", warehouse=self.warehouse)
        self.rack = Rack.objects.create(name="Test Rack", zone=self.zone)
        self.serializer = ShelfSerializer(
            instance=Shelf(name="Test Shelf", rack=self.rack)
        )

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), {"id", "name", "rack"})

    def test_name_field_content(self):
        data = self.serializer.data
        self.assertEqual(data["name"], "Test Shelf")

    def test_rack_field_content(self):
        data = self.serializer.data
        self.assertEqual(data["rack"], self.rack.id)


class RackSerializerTest(TestCase):
    def setUp(self):
        self.warehouse = Warehouse.objects.create(name="Test Warehouse")
        self.zone = Zone.objects.create(name="Test Zone", warehouse=self.warehouse)
        self.serializer = RackSerializer(
            instance=Rack(name="Test Rack", zone=self.zone)
        )

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), {"id", "name", "zone"})

    def test_name_field_content(self):
        data = self.serializer.data
        self.assertEqual(data["name"], "Test Rack")

    def test_zone_field_content(self):
        data = self.serializer.data
        self.assertEqual(data["zone"], self.zone.id)


class ZoneSerializerTest(TestCase):
    def setUp(self):
        self.warehouse = Warehouse.objects.create(name="Test Warehouse")
        self.serializer = ZoneSerializer(
            instance=Zone(name="Test Zone", warehouse=self.warehouse)
        )

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), {"id", "name", "warehouse"})

    def test_name_field_content(self):
        data = self.serializer.data
        self.assertEqual(data["name"], "Test Zone")

    def test_warehouse_field_content(self):
        data = self.serializer.data
        self.assertEqual(data["warehouse"], self.warehouse.id)


class WarehouseSerializerTest(TestCase):
    def setUp(self):
        self.warehouse = Warehouse.objects.create(name="Test Warehouse")
        self.serializer = WarehouseSerializer(instance=self.warehouse)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), {"id", "name"})

    def test_name_field_content(self):
        data = self.serializer.data
        self.assertEqual(data["name"], "Test Warehouse")
