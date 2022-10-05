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
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import *
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.generics import GenericAPIView
from .serializers import RefreshTokenSerializer


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
        return Response({'success':True,'msg':'User successfully deleted!'})

class LogoutView(GenericAPIView):
    serializer_class = RefreshTokenSerializer
    permission_classes = (IsAuthenticated, )

    def post(self, request, *args):
        sz = self.get_serializer(data=request.data)
        sz.is_valid(raise_exception=True)
        sz.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserContact(APIView):
  authentication_classes=[JWTAuthentication]

  def get(self,request):
    if request.user.is_authenticated:
      userserializer = UserContactSerializer(request.user)
      return Response(serializers.data)
    else:
        return Response({'success':False,'msg':status.HTTP_401_UNAUTHORIZED})
        