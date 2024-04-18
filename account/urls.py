from django.urls import path
from .views import ChangePasswordView, DeactivateUserView, UpdateUserView, UserList, AuthUserLoginView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)


urlpatterns = [
    path("auth/adduser/", UserList.as_view(), name = "register"),
    path('auth/login/', AuthUserLoginView.as_view(), name = "login"),
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/users/', UserList.as_view(), name="getallusers"),
    path('auth/change-password/', ChangePasswordView.as_view(), name="change_password"),
    path('auth/update-user/<int:pk>/', UpdateUserView.as_view(), name="update_user"),
    path('auth/deactivate-user/<int:pk>/', DeactivateUserView.as_view(), name="deactivate_user"),
]