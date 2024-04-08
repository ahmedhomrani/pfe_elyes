from django.urls import path
from .views import LigneListCreateAPIView, LigneRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', LigneListCreateAPIView.as_view(), name='ligne-list-create'),
    path('<int:pk>', LigneRetrieveUpdateDestroyAPIView.as_view(), name='ligne-detail'),
]
