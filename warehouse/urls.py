from django.urls import path
from .views import (
    WarehouseListCreateView,
    WarehouseRetrieveUpdateDestroyView,
    ZoneListCreateView,
    ZoneRetrieveUpdateDestroyView,
    RackListCreateView,
    RackRetrieveUpdateDestroyView,
    ShelfListCreateView,
    ShelfRetrieveUpdateDestroyView,
)

urlpatterns = [
    path("warehouses/", WarehouseListCreateView.as_view(), name="warehouses"),
    path(
        "warehouses/<int:pk>/",
        WarehouseRetrieveUpdateDestroyView.as_view(),
        name="warehouse-detail",
    ),
    path("zones/", ZoneListCreateView.as_view(), name="zones"),
    path(
        "zones/<int:pk>/",
        ZoneRetrieveUpdateDestroyView.as_view(),
        name="zone-detail",
    ),
    path("racks/", RackListCreateView.as_view(), name="racks"),
    path(
        "racks/<int:pk>/",
        RackRetrieveUpdateDestroyView.as_view(),
        name="rack-detail",
    ),
    path("shelves/", ShelfListCreateView.as_view(), name="shelves"),
    path(
        "shelves/<int:pk>/",
        ShelfRetrieveUpdateDestroyView.as_view(),
        name="shelve-detail",
    ),
]
