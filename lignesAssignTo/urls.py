from django.urls import path
from .views import (LignesAssigntoListAPIView, LignesAssigntoRetrieveAPIView,
                    LignesAssigntoCreateAPIView, LignesAssigntoUpdateAPIView,
                    LignesAssigntoDestroyAPIView)

urlpatterns = [
    # LigneAssignto CRUD operations
    path('ligne-assignments/', LignesAssigntoListAPIView.as_view(), name='list_assignments'),
    path('ligne-assignments/<int:pk>/', LignesAssigntoRetrieveAPIView.as_view(), name='get_assignment'),
    path('ligne-assignments/create/', LignesAssigntoCreateAPIView.as_view(), name='create_assignment'),
    path('ligne-assignments/update/<int:pk>/', LignesAssigntoUpdateAPIView.as_view(), name='update_assignment'),
    path('ligne-assignments/delete/<int:pk>/', LignesAssigntoDestroyAPIView.as_view(), name='delete_assignment'),
]
