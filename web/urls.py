from django.urls import path
from .views import (ProductsListView,
                    PracticeListView,
                    PrincipleListView,
                    ExperienceListView,
                    ContactsListView
                    )

urlpatterns = [path('products/', ProductsListView.as_view(), name='products'),
               path('practice/', PracticeListView.as_view(), name='practice'),
               path('principle/', PrincipleListView.as_view(), name='principle'),
               path('experience/', ExperienceListView.as_view(), name='experience'),
               path('contacts/', ContactsListView.as_view(), name='contacts')
               ]
