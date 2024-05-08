from django.http import Http404
from rest_framework import generics, status
from rest_framework.response import Response
from .models import LignesAssignto
from .serializers import LignesAssigntoSerializer, LignesAssigntoCreateSerializer, LignesAssigntoUpdateSerializer
from account.permissions import IsAdminUser, IsTechnician  # Assuming permission class

class LignesAssigntoListAPIView(generics.ListAPIView):
    queryset = LignesAssignto.objects.all()
    serializer_class = LignesAssigntoSerializer

class LignesAssigntoRetrieveAPIView(generics.RetrieveAPIView):
    queryset = LignesAssignto.objects.all()
    serializer_class = LignesAssigntoSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        except Http404:
            return Response({"message": "Resource not found"}, status=status.HTTP_200_OK)

class LignesAssigntoCreateAPIView(generics.CreateAPIView):
    queryset = LignesAssignto.objects.all()
    serializer_class = LignesAssigntoCreateSerializer

class LignesAssigntoUpdateAPIView(generics.UpdateAPIView):
    queryset = LignesAssignto.objects.all()
    serializer_class = LignesAssigntoUpdateSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

class LignesAssigntoDestroyAPIView(generics.DestroyAPIView):
    queryset = LignesAssignto.objects.all()
    permission_classes = [IsAdminUser]
