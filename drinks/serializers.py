from rest_framework import serializers
from .models import Kinywa

class KinywaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kinywa
        fields = ['id', 'name', 'description']
