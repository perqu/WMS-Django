from rest_framework.request import Request
from rest_framework import generics, mixins
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated
from django.core.paginator import Paginator


class ProductListCreateView(
    generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin
):

    """
    Endpoint for creating and listing products.
    """

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]

    def get(self, request: Request, *args, **kwargs):
        page_size = request.GET.get("page_size", 10)
        page_number = request.GET.get("page", 1)

        products = self.get_queryset()
        paginator = Paginator(products, page_size)
        page_obj = paginator.get_page(page_number)

        serializer = self.get_serializer(page_obj, many=True)
        return Response(serializer.data)

    def post(self, request: Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProductRetrieveUpdateDeleteView(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):

    """
    Endpoint for editing, deleting and listing product.
    """

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]

    def get(self, request: Request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request: Request, *args, **kwargs):
        kwargs["partial"] = True
        return self.update(request, *args, **kwargs)

    def delete(self, request: Request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
