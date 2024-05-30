from rest_framework import serializers
from .models import Ligne, Test, LigneTest, Banc

# Serializers for Ligne
class LigneCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ligne
        fields = ['id', 'title', 'sem']

class LigneUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ligne
        fields = ['id', 'title', 'sem', 'status']

class LigneRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ligne
        fields = ['id', 'title', 'datecreation', 'sem', 'status']

class LigneDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ligne
        fields = ['id', 'title', 'datecreation', 'sem', 'status']

class LigneListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ligne
        fields = ['id', 'title', 'datecreation', 'sem', 'status']
class LigneForTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LigneTest
        fields = ['id', 'ligne', 'test', 'periodicity']
class BancForLigneTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banc
        fields = ['id', 'ligne_test', 'banc_name', 'validated_by_technician', 'validated_by_validator',
                  'technician', 'validator', 'validation_date', 'revalidation_date', 'validator_visa', 'comment']

class LigneTestForLigneSerializer(serializers.ModelSerializer):
    class Meta:
        model = LigneTest
        fields = ['id', 'ligne', 'test', 'periodicity']
        

# Serializers for Test
class TestCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ['id', 'name', 'nbr_banc']

class TestUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ['id', 'name', 'nbr_banc']

class TestRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ['id', 'name', 'nbr_banc']

class TestListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ['id', 'name', 'nbr_banc']

# Serializers for LigneTest
class LigneTestCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LigneTest
        fields = ['ligne', 'test', 'periodicity']

class LigneTestRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = LigneTest
        fields = ['id', 'ligne', 'test', 'periodicity']

class LigneTestListSerializer(serializers.ModelSerializer):
    class Meta:
        model = LigneTest
        fields = ['id', 'ligne', 'test', 'periodicity']

# Serializers for Banc
class BancCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banc
        fields = [
            'ligne_test', 'banc_name', 'validated_by_technician', 'validated_by_validator',
            'technician', 'validator', 'validation_date', 'revalidation_date', 'validator_visa', 'comment'
        ]
from .models import User
class BancRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banc
        fields = '__all__'

    def update(self, instance, validated_data):
        # Get the authenticated user from the request
        user = self.context['request'].user

        # Check if the user is a technician or validator
        if user.role == User.TECHNICIEN:
            instance.technician = user
        elif user.role == User.VALIDATEUR:
            instance.validator = user

        # Perform the update
        instance.save()
        return instance

class BancListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banc
        fields = [
            'id', 'ligne_test', 'banc_name', 'validated_by_technician', 'validated_by_validator',
            'technician', 'validator', 'validation_date', 'revalidation_date', 'validator_visa', 'comment'
        ]
