# from lignesAssignTo.models import LignesAssignto
# from rest_framework import serializers
# from account.models import User

# class LignesAssigntoSerializer(serializers.ModelSerializer):
#     ligne_title = serializers.CharField(source='ligne.title', read_only=True)
#     technician_username = serializers.CharField(source='technician.username', read_only=True)

#     class Meta:
#         model = LignesAssignto
#         fields = ['id', 'ligne', 'ligne_title', 'technician', 'technician_username', 'status', 'realisation_date', 'comment', 'affectation_date','confirmed']

# class LignesAssigntoCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = LignesAssignto
#         fields = ['ligne', 'technician', 'status']  # Avoid including realization_date initially

# class LignesAssigntoUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = LignesAssignto
#         fields = ['status', 'realisation_date', 'comment']  # Update status, realization date, and comment