from netapi.views.front_views import *
from django.urls import path
urlpatterns=[
    path('list/',ServerViewSet.as_view({'get':'list'}),name='list'),
    path('create/',ServerViewSet.as_view({'post':'create'}),name='create'),
    path('retrieve/<int:pk>/',ServerViewSet.as_view({'get':'retrieve'}),name="retrieve"),
    path('delete/<int:pk>/',ServerViewSet.as_view({'get':'destroy'}),name='delete')
]