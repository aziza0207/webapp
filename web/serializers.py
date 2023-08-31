from rest_framework import serializers
from .models import Principle, Experience, Products, Practice


class PrincipleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Principle
        fields = ['title', 'image', 'description']


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ['title']


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['image', 'title', 'description']


class PracticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Practice
        fields = ['title',
                  'image',
                  'description']
