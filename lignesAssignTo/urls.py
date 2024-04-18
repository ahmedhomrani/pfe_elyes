from django.urls import path
from .views import (LignesAssigntoListAPIView, LignesAssigntoRetrieveAPIView,
                    LignesAssigntoCreateAPIView, LignesAssigntoUpdateAPIView,
                    LignesAssigntoDestroyAPIView)

urlpatterns = [
    # LigneAssignto CRUD operations
    path('', LignesAssigntoListAPIView.as_view(), name='list_assignments'),
    path('get/<int:pk>', LignesAssigntoRetrieveAPIView.as_view(), name='get_assignment'),
    path('create/', LignesAssigntoCreateAPIView.as_view(), name='create_assignment'),
    path('update/<int:pk>/', LignesAssigntoUpdateAPIView.as_view(), name='update_assignment'),
    path('delete/<int:pk>/', LignesAssigntoDestroyAPIView.as_view(), name='delete_assignment'),
]
