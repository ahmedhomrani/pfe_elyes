from .serializers import UserSerializers, UserLoginSerializer, UserUpdateSerializer
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .serializers import UserSerializers, UserLoginSerializer, PasswordChangeSerializer
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from .serializers import UserSerializers, UserLoginSerializer, PasswordChangeSerializer, UserUpdateSerializer
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.permissions import IsAuthenticated

from account import serializers


class TokenRefreshAPIView(TokenRefreshView):
    pass

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        user = serializer.save()

        # Send simple email to the newly registered user
        subject = 'Welcome to Our Platform!'
        message = 'Thank you for registering with us. Your username is {}.'.format(user.username)
        recipient_list = [user.email]
        send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)


class AuthUserLoginView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            password = serializer.validated_data.get('password')
            user = authenticate(email=email, password=password)

            if user is not None:
                # If the user is authenticated, generate tokens
                refresh = RefreshToken.for_user(user)

                response = {
                    'success': True,
                    'message': 'User logged in successfully',
                    'email': email,
                    'role': user.role,
                    'id':user.id,
                    'access_token': str(refresh.access_token),
                    'refresh_token': str(refresh)
                }
                return Response(response, status=status.HTTP_200_OK)
            else:
                # If authentication fails, return appropriate error message
                return Response({'message': ['Invalid login credentials']}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class ChangePasswordView(APIView):
    serializer_class = PasswordChangeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = request.user
            old_password = serializer.validated_data.get('old_password')
            new_password = serializer.validated_data.get('new_password')

            if not user.check_password(old_password):
                return Response({'message': ['Old password is incorrect']}, status=status.HTTP_400_BAD_REQUEST)

            user.set_password(new_password)
            user.save()

            return Response({'success': True, 'message': 'Password changed successfully'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateUserView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer  
    permission_classes = [permissions.IsAuthenticated & permissions.IsAdminUser]

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
class DeactivateUserView(generics.DestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated & permissions.IsAdminUser]

    def destroy(self, request, *args, **kwargs):
        # Check if the requesting user has admin role
        if not request.user.is_staff:
            return Response({'message': 'Access forbidden'}, status=status.HTTP_403_FORBIDDEN)
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        return Response({'message': 'User deactivated successfully'}, status=status.HTTP_200_OK)
    
class DeleteUserView(generics.DestroyAPIView):
    queryset = User.objects.all()

    def destroy(self, request, *args, **kwargs):
        # Check if the requesting user has admin role
        instance = self.get_object()
        if instance.role == User.ADMIN:
            return Response({'message': 'Access forbidden you cannot delete admin'}, status=status.HTTP_403_FORBIDDEN)
        instance.delete_user()  # Call the delete_user method to permanently delete the user
        return Response({'message': 'User deleted successfully'}, status=status.HTTP_200_OK)