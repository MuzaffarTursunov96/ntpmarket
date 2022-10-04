import imp
from django.urls import path, include,re_path
from .views import *
from projects.views import UserGetMe

urlpatterns = [
  path('register/', RegisterView.as_view(), name='auth_register'),
  path('login/', LoginView.as_view(), name='token_obtain_pair'),
  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  path('api-auth/', include('rest_framework.urls')),
  path('me',UserGetMe.as_view(),name='get-me'),
  path('delete-account',DeleteAccount.as_view(),name='delete-account'),
  # path('logout/', LogoutView.as_view(), name='auth_logout'),
  
]
