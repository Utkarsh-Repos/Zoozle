import string
import random

from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt

from .serializers import CreateUser, ListSerializer, DetailSerializer, LoginSerializers
from django.contrib.auth.models import User
from account.models import UserPhone


class AccountCreation(viewsets.ViewSet):

    def create(self, request):
        serialized_data = CreateUser(data=request.data)
        if serialized_data.is_valid(raise_exception=True):
            validated_data = serialized_data.validated_data
            validated_data_email = validated_data['email']
            try:
                obj = User.objects.get(email =validated_data_email)
            except User.DoesNotExist:
                random_chars = random.choices(string.ascii_letters, k=2)
                random_string = ''.join(random_chars)
                username = str(validated_data['phone_number']) + random_string
                user = User.objects.create(username=username,
                                           email=str(validated_data['email']),
                                           first_name=str(validated_data['first_name'])
                                           )
                user.set_password(str(validated_data['password']))
                user.save()
                user_phone_obj = UserPhone.objects.create(user_detail=user,
                                                          phone_number=int(validated_data['phone_number']))
                return Response({'result': 'data created successfully'})
            return Response({'result': 'data Already exist'})


    def list(self, request):
        obj = User.objects.all()
        serialiazed_data = ListSerializer(obj, many=True)
        return Response(serialiazed_data.data)

    def destroy(self, request, *args, **kwargs):
        coupon_object = get_object_or_404(User, pk=int(kwargs['pk']))
        coupon_object.delete()
        return Response({'result': 'deleted successfully'})


class DetailData(APIView):
    def get(self, request):
        obj = User.objects.filter(is_superuser=False)
        serialized_data = DetailSerializer(obj, many=True)
        return Response(serialized_data.data)



class LoginApi(APIView):

    def post(self, request):
        serialized_data = LoginSerializers(data=request.data)
        if serialized_data.is_valid():
            validated = serialized_data.validated_data
            username = User.objects.filter(email=str(validated['email']))
            if username.exists():
                user = authenticate(request, username=str(username[0].username), password=validated['password'])
                if user:
                    login(request, user)
                    return Response({'result': 'authenticated'})
                else:
                    return Response({'result': 'not authenticated'})
            else:
                return Response({'result': 'not authenticated'})

