from rest_framework import serializers
from .models import (Principle,
                     Experience,
                     Products,
                     Practice,
                     Contacts,
                     Value,
                     Photo,
                     Video)


class PrincipleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Principle
        fields = ['title']


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


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ['phone',
                  'email',
                  'address']


class ValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Value
        fields = ['title']


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['url']


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['url']
