from lignesAssignTo.models import LignesAssignto
from account.models import User
from lignesAssignTo.serializers import LignesAssigntoSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Ligne
from .serializers import  LigneDetailSerializer, LigneListSerializer, LigneRetrieveSerializer, LigneCreateSerializer, LigneUpdateSerializer
from .permissions import IsAdminUser
from rest_framework.exceptions import  AuthenticationFailed


class LigneRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ligne.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return LigneDetailSerializer  # Use detail serializer for GET requests
        return LigneRetrieveSerializer  # Use default serializer for other methods

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            # Include related LignesAssignto data
            serializer.data['assignments'] = LignesAssigntoSerializer(
                instance.assignments.all(), many=True).data
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



class LigneListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ligne.objects.all()
    serializer_class = LigneListSerializer
    permission_classes = [IsAdminUser]

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                data = serializer.validated_data
                technician_id = data.pop('technician', None)  # Remove technician ID from data

                ligne = Ligne.objects.create(**data)  # Create the Ligne object

                # Check if technician ID is provided and valid
                if technician_id:
                    try:
                        technician = User.objects.get(pk=technician_id, role=User.TECHNICIEN)
                        # Create assignment with technician and pending status
                        LignesAssignto.objects.create(
                            ligne=ligne,
                            technician=technician,
                            status='pending',
                            realisation_date=None
                        )
                    except User.DoesNotExist:
                        return Response({'error': 'Technician not found'}, status=status.HTTP_404_NOT_FOUND)
                    except Exception as e:
                        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

                return Response({"message": "Line created successfully.", "id": ligne.id}, status=status.HTTP_201_CREATED)
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

    def list(self, request, *args, **kwargs):
        try:
            lignes = self.get_queryset()
            serializer = self.get_serializer(lignes, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)