from rest_framework import generics
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
    queryset = Products.objects.all()


class PracticeListView(generics.ListAPIView):
    serializer_class = PracticeSerializer
    queryset = Practice.objects.all()


class PrincipleListView(generics.ListAPIView):
    serializer_class = PrincipleSerializer
    queryset = Principle.objects.all()


class ExperienceListView(generics.ListAPIView):
    serializer_class = ExperienceSerializer
    queryset = Experience.objects.all()


class ContactsListView(generics.ListAPIView):
    serializer_class = ContactsSerializer
    queryset = Contacts.objects.all()


class ValueListView(generics.ListAPIView):
    serializer_class = ValueSerializer
    queryset = Value.objects.all()


class PhotoView(generics.ListAPIView):
    serializer_class = PhotoSerializer
    queryset = Photo.objects.all()


class VideoView(generics.ListAPIView):
    serializer_class = VideoSerializer
    queryset = Video.objects.all()
