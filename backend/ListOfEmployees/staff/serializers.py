from .models import Person
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = [
        'first_name',
        'surname',
        'patronymic',
        'phonenumber',
        'image',
        'date_of_birth',
        'status',
        ]