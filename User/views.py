from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import LoginSerializer, MyUserSerializer,UserDetailsChangeSerializer,UserChangePasswordSerializer
from .models import MyUser

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

# Create your views here.
class SignUp(APIView):
    def post(self,request,*args,**kwargs):
        data = MyUserSerializer(data=request.data)
        data.is_valid(raise_exception=True)
        data.save()
        return Response(status=status.HTTP_201_CREATED)

class LoginView(APIView):
    def post(self,request,*args,**kwargs):
        demail = request.data.get('email')
        dpassword = request.data.get('password')       
        user = authenticate(email=demail,password=dpassword)
        if user is not None:
            token = get_tokens_for_user(user)
            data = MyUser.objects.get(id=user.id)
            sdata = LoginSerializer(data)
            return Response({'token':token,'status':status.HTTP_200_OK})
        return Response('Incorrect credentials')

class UserView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,*args,**kwargs):
        data = MyUser.objects.get(id = request.user.id)
        sdata = LoginSerializer(data)
        return Response({'data':sdata.data,'status':status.HTTP_200_OK})

    def patch(self,request,*args,**kwargs):
        data = MyUser.objects.get(id = request.user.id)
        sdata = UserDetailsChangeSerializer(data,data=request.data,partial=True)
        sdata.is_valid(raise_exception=True)
        sdata.save()
        return Response({'data':sdata.data,'status':status.HTTP_201_CREATED})

class UserPasswordChangeView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request,*args,**kwargs):
        data = MyUser.objects.get(id = request.user.id)
        sdata = UserChangePasswordSerializer(data=request.data,context = {'user':data})
        sdata.is_valid(raise_exception=True)
        sdata.save()
        print('hello world')
        return Response(status = status.HTTP_200_OK)

        