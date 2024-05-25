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
        fields = ['id', 'title', 'sem']

class LigneRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ligne
        fields = ['id', 'title', 'datecreation', 'sem']

class LigneDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ligne
        fields = ['id', 'title', 'datecreation', 'sem']

class LigneListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ligne
        fields = ['id', 'title', 'datecreation', 'sem']

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

class BancRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banc
        fields = [
            'id', 'ligne_test', 'banc_name', 'validated_by_technician', 'validated_by_validator',
            'technician', 'validator', 'validation_date', 'revalidation_date', 'validator_visa', 'comment'
        ]

class BancListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banc
        fields = [
            'id', 'ligne_test', 'banc_name', 'validated_by_technician', 'validated_by_validator',
            'technician', 'validator', 'validation_date', 'revalidation_date', 'validator_visa', 'comment'
        ]
