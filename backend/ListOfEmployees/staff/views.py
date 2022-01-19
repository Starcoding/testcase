from django.shortcuts import render
from rest_framework import viewsets, filters, generics
from .models import Person
from .serializers import PersonSerializer
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = [
        'first_name',
        'surname',
        'patronymic',
        'phonenumber',
        'date_of_birth',
        'status',
        ]
    search_fields = [
        'first_name',
        'surname',
        'patronymic',
        'phonenumber',
        'date_of_birth',
        'status',
        ]
    