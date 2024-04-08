from .serializers import UserSerializers, UserLoginSerializer
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .serializers import UserSerializers, UserLoginSerializer, PasswordChangeSerializer
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [permissions.AllowAny]

    def list(self, request, *args, **kwargs):
        # Check if the requesting user has admin role
        if request.user.role != User.ADMIN:
            return Response({'message': 'Access forbidden'}, status=status.HTTP_403_FORBIDDEN)
        return super().list(request, *args, **kwargs)


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
                    'access_token': str(refresh.access_token),
                    'refresh_token': str(refresh)
                }
                return Response(response, status=status.HTTP_200_OK)
            else:
                # If authentication fails, return appropriate error message
                return Response({'non_field_errors': ['Invalid login credentials']}, status=status.HTTP_401_UNAUTHORIZED)
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
                return Response({'non_field_errors': ['Old password is incorrect']}, status=status.HTTP_400_BAD_REQUEST)

            user.set_password(new_password)
            user.save()

            return Response({'success': True, 'message': 'Password changed successfully'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
