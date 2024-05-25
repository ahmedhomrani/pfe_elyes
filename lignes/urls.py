from django.urls import path

from .views import LigneListCreateAPIView, LigneRetrieveUpdateDestroyAPIView, TestListCreateAPIView, TestRetrieveUpdateDestroyAPIView
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
]
