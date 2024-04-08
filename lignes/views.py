from rest_framework import generics, status
from rest_framework.response import Response
from .models import Ligne
from .serializers import  LigneRetrieveSerializer, LigneCreateSerializer, LigneUpdateSerializer
from .permissions import IsAdminUser
from rest_framework.exceptions import  AuthenticationFailed

class LigneListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ligne.objects.all()
    serializer_class = LigneCreateSerializer
    permission_classes = [IsAdminUser]

    def list(self, request, *args, **kwargs):
        try:
            lignes = self.get_queryset()
            serializer = LigneRetrieveSerializer(lignes, many=True)  # Use Retrieve Serializer here
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Line created successfully."}, status=status.HTTP_201_CREATED)
            else:
                return Response({"error": "Failed to create line. Please check your input data."},
                                status=status.HTTP_400_BAD_REQUEST)
        except AuthenticationFailed:
            # If the error is due to authentication/token issues
            return Response({"error": "Unauthorized. Please provide a valid authentication token."},
                            status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            # If the error is from the server
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class LigneRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ligne.objects.all()
    serializer_class = LigneRetrieveSerializer
    permission_classes = [IsAdminUser]

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Ligne.DoesNotExist:
            return Response({'error': 'Ligne not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Ligne.DoesNotExist:
            return Response({'error': 'Ligne not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Ligne.DoesNotExist:
            return Response({'error': 'Ligne not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
