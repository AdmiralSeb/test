from rest_framework import serializers
from .models import PetInfo, PetHealth, Product

class PetInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetInfo
        fields = '__all__'

class PetHealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetHealth
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
