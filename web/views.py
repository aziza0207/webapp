from rest_framework import generics
from django.utils import translation
from .models import (Products,
                     Practice,
                     Principle,
                     Experience,
                     Contacts,
                     Value,
                     Photo,
                     Video)
from .serializers import (ProductsSerializer,
                          PracticeSerializer,
                          ExperienceSerializer,
                          PrincipleSerializer,
                          ContactsSerializer,
                          ValueSerializer,
                          VideoSerializer,
                          PhotoSerializer
                          )


class ProductsListView(generics.ListAPIView):
    serializer_class = ProductsSerializer

    def get_queryset(self):
        queryset = Products.objects.all()
        if 'HTTP_ACCEPT_LANGUAGE' in self.request.META:
            lang = self.request.META['HTTP_ACCEPT_LANGUAGE']
            translation.activate(lang)
        return queryset


class PracticeListView(generics.ListAPIView):
    serializer_class = PracticeSerializer

    def get_queryset(self):
        queryset = Practice.objects.all()
        if 'HTTP_ACCEPT_LANGUAGE' in self.request.META:
            lang = self.request.META['HTTP_ACCEPT_LANGUAGE']
            translation.activate(lang)
        return queryset


class PrincipleListView(generics.ListAPIView):
    serializer_class = PrincipleSerializer

    def get_queryset(self):
        queryset = Principle.objects.all()
        if 'HTTP_ACCEPT_LANGUAGE' in self.request.META:
            lang = self.request.META['HTTP_ACCEPT_LANGUAGE']
            translation.activate(lang)
        return queryset


class ExperienceListView(generics.ListAPIView):
    serializer_class = ExperienceSerializer

    def get_queryset(self):
        queryset = Experience.objects.all()
        if 'HTTP_ACCEPT_LANGUAGE' in self.request.META:
            lang = self.request.META['HTTP_ACCEPT_LANGUAGE']
            translation.activate(lang)
        return queryset


class ContactsListView(generics.ListAPIView):
    serializer_class = ContactsSerializer

    def get_queryset(self):
        queryset = Contacts.objects.all()
        if 'HTTP_ACCEPT_LANGUAGE' in self.request.META:
            lang = self.request.META['HTTP_ACCEPT_LANGUAGE']
            translation.activate(lang)
        return queryset


class ValueListView(generics.ListAPIView):
    serializer_class = ValueSerializer

    def get_queryset(self):
        queryset = Value.objects.all()
        if 'HTTP_ACCEPT_LANGUAGE' in self.request.META:
            lang = self.request.META['HTTP_ACCEPT_LANGUAGE']
            translation.activate(lang)
        return queryset


class PhotoView(generics.ListAPIView):
    serializer_class = PhotoSerializer
    queryset = Photo.objects.all()


class VideoView(generics.ListAPIView):
    serializer_class = VideoSerializer
    queryset = Video.objects.all()
