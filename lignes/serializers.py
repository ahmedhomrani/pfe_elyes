from lignesAssignTo.serializers import LignesAssigntoSerializer
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
class LigneDetailSerializer(LigneRetrieveSerializer):
    assignments = LignesAssigntoSerializer(source='assignments.all', many=True)

    class Meta(LigneRetrieveSerializer.Meta):
        fields = (*LigneRetrieveSerializer.Meta.fields, 'assignments')

class LigneListSerializer(serializers.ModelSerializer):
    assignments_count = serializers.SerializerMethodField()

    class Meta:
        model = Ligne
        fields = ['id', 'title', 'daterealisation', 'datecreation', 'assignments_count']

    def get_assignments_count(self, obj):
        return obj.assignments.count()