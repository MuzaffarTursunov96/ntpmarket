from django.urls import path, include,re_path
from rest_framework_jwt.views import verify_jwt_token
from .views import *

urlpatterns = [
  path('register/', RegisterView.as_view(), name='auth_register'),
  path('login/', LoginView.as_view(), name='token_obtain_pair'),
  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  path('api-auth/', include('rest_framework.urls')),
  # re_path(r'^api-token-verify/', verify_jwt_token),
]
