from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from .models import Ligne, Test, LigneTest, Banc
from .serializers import (
    BancForLigneTestSerializer, LigneCreateSerializer, LigneForTestSerializer, LigneTestForLigneSerializer, LigneUpdateSerializer, LigneRetrieveSerializer, LigneDetailSerializer, LigneListSerializer,
    TestCreateSerializer, TestUpdateSerializer, TestRetrieveSerializer, TestListSerializer,
    LigneTestCreateSerializer, LigneTestRetrieveSerializer, LigneTestListSerializer,
    BancCreateSerializer, BancRetrieveSerializer, BancListSerializer
)

# Ligne Views
class LigneTestsByLigneAPIView(generics.ListAPIView):
    serializer_class = LigneTestForLigneSerializer

    def get_queryset(self):
        ligne_id = self.kwargs['pk']
        return LigneTest.objects.filter(ligne_id=ligne_id)
class BancsByLigneTestAPIView(generics.ListAPIView):
    serializer_class = BancForLigneTestSerializer

    def get_queryset(self):
        ligne_test_id = self.kwargs['pk']
        return Banc.objects.filter(ligne_test_id=ligne_test_id)
class LignesByTestAPIView(generics.ListAPIView):
    serializer_class = LigneForTestSerializer

    def get_queryset(self):
        test_id = self.kwargs['pk']
        return LigneTest.objects.filter(test_id=test_id)    

class LigneListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ligne.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return LigneCreateSerializer
        return LigneListSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LigneRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ligne.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return LigneDetailSerializer
        return LigneUpdateSerializer
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# Test Views
class TestListCreateAPIView(generics.ListCreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestListSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TestCreateSerializer
        return TestListSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TestRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Test.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TestRetrieveSerializer
        return TestUpdateSerializer
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

# LigneTest Views
class LigneTestListCreateAPIView(generics.ListCreateAPIView):
    queryset = LigneTest.objects.all()
    serializer_class = LigneTestListSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return LigneTestCreateSerializer
        return LigneTestListSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LigneTestRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LigneTest.objects.all()
    serializer_class = LigneTestRetrieveSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return LigneTestRetrieveSerializer
        return LigneTestCreateSerializer
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

# Banc Views
class BancListCreateAPIView(generics.ListCreateAPIView):
    queryset = Banc.objects.all()
    serializer_class = BancListSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return BancCreateSerializer
        return BancListSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BancRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Banc.objects.all()
    serializer_class = BancRetrieveSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BancRetrieveSerializer
        return BancCreateSerializer
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
