from django.conf import settings
from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation



class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id","email","first_name", "last_name","password" ,"username", "role","is_active"]

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = User.objects.create(**validated_data)
        
        # Validate and set the password
        if password:
            try:
                password_validation.validate_password(password, user)
            except ValidationError as e:
                raise serializers.ValidationError({'password': list(e.messages)})
            user.set_password(password)
            user.save()

        # Send email to the newly registered user
        subject = 'Welcome to Our Platform!'
        message = f'Thank you for registering with us.\n\nYour login credentials are:\n\nEmail: {user.email}\nPassword: {password}\nRole: {user.get_role_display()}\n\nPlease keep your credentials safe and chage them please.'
        recipient_list = [user.email]
        send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)

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

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']  # Add other fields you want to update

    def update(self, instance, validated_data):
        # Update the user instance with the validated data
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.role = validated_data.get('role', instance.role)
        instance.password = validated_data.get('password', instance.password)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()
        return instance