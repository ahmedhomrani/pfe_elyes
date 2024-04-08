from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate



#creating serializers.


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["email","first_name", "last_name","password" ,"username", "role"]

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            role=validated_data['role']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)


    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        # Return the validated email and password
        return {'email': email, 'password': password}
    

class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=128, write_only=True)
    new_password = serializers.CharField(max_length=128, write_only=True)

