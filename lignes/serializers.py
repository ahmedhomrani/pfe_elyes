from rest_framework import serializers
from .models import Ligne

class LigneCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ligne
        fields = ['title', 'daterealisation']

class LigneUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ligne
        fields = ['id', 'title', 'daterealisation']

class LigneRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ligne
        fields = ['id', 'title', 'daterealisation', 'datecreation']
