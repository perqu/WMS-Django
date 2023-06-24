from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for the Product model.
    It defines the fields to be included in the serialized representation of a Product instance.
    The Meta class specifies the model to be serialized and the fields to be included.
    In this case, we're including all fields of the Product model by using the "__all__" shortcut.
    """

    class Meta:
        model = Product
        fields = "__all__"
