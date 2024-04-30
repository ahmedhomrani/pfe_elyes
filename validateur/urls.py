# urls.py in validateur app
from django.urls import path
from .views import VerificationCreateAPIView

urlpatterns = [
    path('create/', VerificationCreateAPIView.as_view(), name='create_verification'),
]
