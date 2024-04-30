# views.py in validateur app
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import VerificationSerializer
from lignesAssignTo.models import LignesAssignto

class VerificationCreateAPIView(APIView):
    def post(self, request, format=None):
        serializer = VerificationSerializer(data=request.data)
        if serializer.is_valid():
            # Create verification instance
            verification_instance = serializer.save()

            # Update LignesAssignto instance
            lignes_assignto_id = request.data.get('lignes_assignto')
            try:
                lignes_assignto = LignesAssignto.objects.get(id=lignes_assignto_id)
                lignes_assignto.confirmed = True
                lignes_assignto.save()
            except LignesAssignto.DoesNotExist:
                # Handle if LignesAssignto instance does not exist
                pass

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
