from django.test import TestCase
from products.models import Product
from warehouse.models import Warehouse, Zone, Rack, Shelf, ProductStorageLink


class WarehouseModelTest(TestCase):
    def test_name_field(self):
        warehouse = Warehouse.objects.create(name="Test Warehouse")
        self.assertEqual(warehouse.name, "Test Warehouse")


class ZoneModelTest(TestCase):
    def setUp(self):
        self.warehouse = Warehouse.objects.create(name="Test Warehouse")

    def test_name_field(self):
        zone = Zone.objects.create(name="Test Zone", warehouse=self.warehouse)
        self.assertEqual(zone.name, "Test Zone")

    def test_warehouse_foreign_key(self):
        zone = Zone.objects.create(name="Test Zone", warehouse=self.warehouse)
        self.assertEqual(zone.warehouse, self.warehouse)


class RackModelTest(TestCase):
    def setUp(self):
        self.warehouse = Warehouse.objects.create(name="Test Warehouse")
        self.zone = Zone.objects.create(name="Test Zone", warehouse=self.warehouse)

    def test_name_field(self):
        rack = Rack.objects.create(name="Test Rack", zone=self.zone)
        self.assertEqual(rack.name, "Test Rack")

    def test_zone_foreign_key(self):
        rack = Rack.objects.create(name="Test Rack", zone=self.zone)
        self.assertEqual(rack.zone, self.zone)


class ShelfModelTest(TestCase):
    def setUp(self):
        self.warehouse = Warehouse.objects.create(name="Test Warehouse")
        self.zone = Zone.objects.create(name="Test Zone", warehouse=self.warehouse)
        self.rack = Rack.objects.create(name="Test Rack", zone=self.zone)

    def test_name_field(self):
        shelf = Shelf.objects.create(name="Test Shelf", rack=self.rack)
        self.assertEqual(shelf.name, "Test Shelf")

    def test_rack_foreign_key(self):
        shelf = Shelf.objects.create(name="Test Shelf", rack=self.rack)
        self.assertEqual(shelf.rack, self.rack)


class ProductStorageLinkModelTest(TestCase):
    def setUp(self):
        self.warehouse = Warehouse.objects.create(name="Test Warehouse")
        self.zone = Zone.objects.create(name="Test Zone", warehouse=self.warehouse)
        self.rack = Rack.objects.create(name="Test Rack", zone=self.zone)
        self.shelf = Shelf.objects.create(name="Test Shelf", rack=self.rack)
        self.product = Product.objects.create(name="Test Product", price=9.99)

    def test_product_foreign_key(self):
        link = ProductStorageLink.objects.create(
            product=self.product, shelf=self.shelf, quantity=10
        )
        self.assertEqual(link.product, self.product)

    def test_shelf_foreign_key(self):
        link = ProductStorageLink.objects.create(
            product=self.product, shelf=self.shelf, quantity=10
        )
        self.assertEqual(link.shelf, self.shelf)

    def test_quantity_field(self):
        link = ProductStorageLink.objects.create(
            product=self.product, shelf=self.shelf, quantity=10
        )
        self.assertEqual(link.quantity, 10)
