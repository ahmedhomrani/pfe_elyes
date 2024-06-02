from django.urls import path

from .views import BancsByLigneTestAPIView, GeneratePDF, GeneratePDFLigne, LigneListCreateAPIView, LigneRetrieveUpdateDestroyAPIView, LigneTestsByLigneAPIView, LignesByTestAPIView, TestListCreateAPIView, TestRetrieveUpdateDestroyAPIView
from .views import (
    BancListCreateAPIView, BancRetrieveUpdateDestroyAPIView, 
    LigneListCreateAPIView, LigneRetrieveUpdateDestroyAPIView, 
    LigneTestListCreateAPIView, LigneTestRetrieveUpdateDestroyAPIView, 
    TestListCreateAPIView, TestRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path('', LigneListCreateAPIView.as_view(), name='ligne-list-create'),
    path('<int:pk>', LigneRetrieveUpdateDestroyAPIView.as_view(), name='ligne-detail'),
    path('tests/', TestListCreateAPIView.as_view(), name='test-list-create'),
    path('tests/<int:pk>/', TestRetrieveUpdateDestroyAPIView.as_view(), name='test-detail'),
    path('ligne-tests/', LigneTestListCreateAPIView.as_view(), name='ligne-test-list-create'),
    path('ligne-tests/<int:pk>/', LigneTestRetrieveUpdateDestroyAPIView.as_view(), name='ligne-test-detail'),
    path('bancs/', BancListCreateAPIView.as_view(), name='banc-list-create'),
    path('bancs/<int:pk>/', BancRetrieveUpdateDestroyAPIView.as_view(), name='banc-detail'),
    path('ligne/<int:pk>/', LigneTestsByLigneAPIView.as_view(), name='ligne-tests-by-ligne'),
    path('ligne-tests/test/<int:pk>/', LignesByTestAPIView.as_view(), name='ligne-tests-by-ligne'),
    path('banc/ligne-tests/<int:pk>/', BancsByLigneTestAPIView.as_view(), name='bancs-by-ligne-test'),
    path('pdf', GeneratePDFLigne.as_view(), name='pdf'),
    path('pdf/all', GeneratePDF.as_view(), name='pdf-all'),
]
