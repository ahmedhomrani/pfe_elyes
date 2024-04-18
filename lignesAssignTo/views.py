from rest_framework import generics, status
from rest_framework.response import Response
from .models import LignesAssignto
from .serializers import LignesAssigntoSerializer, LignesAssigntoCreateSerializer, LignesAssigntoUpdateSerializer
from account.permissions import IsAdminUser  # Assuming permission class

class LignesAssigntoListAPIView(generics.ListAPIView):
    queryset = LignesAssignto.objects.all()
    serializer_class = LignesAssigntoSerializer
    permission_classes = [IsAdminUser]

class LignesAssigntoRetrieveAPIView(generics.RetrieveAPIView):
    queryset = LignesAssignto.objects.all()
    serializer_class = LignesAssigntoSerializer
    permission_classes = [IsAdminUser]

class LignesAssigntoCreateAPIView(generics.CreateAPIView):
    queryset = LignesAssignto.objects.all()
    serializer_class = LignesAssigntoCreateSerializer
    permission_classes = [IsAdminUser]

class LignesAssigntoUpdateAPIView(generics.UpdateAPIView):
    queryset = LignesAssignto.objects.all()
    serializer_class = LignesAssigntoUpdateSerializer
    permission_classes = [IsAdminUser]

class LignesAssigntoDestroyAPIView(generics.DestroyAPIView):
    queryset = LignesAssignto.objects.all()
    permission_classes = [IsAdminUser]
