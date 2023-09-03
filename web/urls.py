from django.urls import path
from .views import (ProductsListView,
                    PracticeListView,
                    PrincipleListView,
                    ExperienceListView,
                    ContactsListView,
                    ValueListView,
                    PhotoView,
                    VideoView
                    )

urlpatterns = [path('products/', ProductsListView.as_view(), name='products'),
               path('practice/', PracticeListView.as_view(), name='practice'),
               path('principle/', PrincipleListView.as_view(), name='principle'),
               path('experience/', ExperienceListView.as_view(), name='experience'),
               path('contacts/', ContactsListView.as_view(), name='contacts'),
               path('values/', ValueListView.as_view(), name='values'),
               path('photo/', PhotoView.as_view(), name='photo'),
               path('video/', VideoView.as_view(), name='video')
               ]
