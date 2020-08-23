from rest_framework import serializers

from ...models import *


class HomePageBannerSliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomePageBannerSlider
        fields = '__all__'


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'


class ProductVariantSerializer(serializers.ModelSerializer):
    height_with_unit = serializers.CharField(read_only=True)
    length_with_unit = serializers.CharField(read_only=True)
    width_with_unit = serializers.CharField(read_only=True)
    weight_with_unit = serializers.CharField(read_only=True)

    class Meta:
        model = ProductVariant
        fields = '__all__'


class ProductImageializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    variants = ProductVariantSerializer(source='product_variants', many=True)
    images = ProductImageializer(source='product_images', many=True)

    class Meta:
        model = Product
        fields = '__all__'
