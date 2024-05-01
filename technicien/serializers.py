from rest_framework import serializers
from lignesAssignTo.models import LignesAssignto

class LignesAssigntoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LignesAssignto
        fields = ['status', 'realisation_date', 'comment', 'confirmed']