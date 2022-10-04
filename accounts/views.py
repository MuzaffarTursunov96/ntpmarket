# from django.shortcuts import render

# Create your views here.
from projects.models import Projects, UserBiddings, Wishlist
from .models import User
from .serializers import RegisterSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .serializers import *
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

class DeleteAccount(APIView):

    def post(self,request):
        id =request.data['id']
        user =get_object_or_404(User,id=id)
        projects=Projects.objects.filter(creator=user)
        projects.delete()
        biddings =UserBiddings.objects.filter(user=user)
        biddings.delete()
        wishlists = Wishlist.objects.filter(user=user)
        wishlists.delete()
        user.delete()
