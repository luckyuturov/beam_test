from rest_framework import serializers
from .models import Category, Product, Vendor


class CategorySerializer(serializers.ModelSerializer):
    vendors = serializers.PrimaryKeyRelatedField(many=True, queryset=Vendor.objects.all())

    class Meta:
        model = Category
        fields = '__all__'


class VendorSerializer(serializers.ModelSerializer):
    categories = serializers.PrimaryKeyRelatedField(many=True, queryset=Category.objects.all())

    class Meta:
        model = Vendor
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    vendor = serializers.PrimaryKeyRelatedField(queryset=Vendor.objects.all(), allow_null=True, required=False)

    class Meta:
        model = Product
        fields = '__all__'
