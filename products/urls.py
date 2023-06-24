from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.ProductListCreateView.as_view(), name="products"),
    path(
        "products/<int:pk>/",
        views.ProductRetrieveUpdateDeleteView.as_view(),
        name="product-detail",
    ),
]
