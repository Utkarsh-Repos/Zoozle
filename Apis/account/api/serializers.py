from rest_framework import serializers
from account.models import UserPhone

class CreateUser(serializers.Serializer):
    password = serializers.CharField(max_length=200, required=True)
    email = serializers.CharField(max_length=200, required=True)
    first_name = serializers.CharField(max_length=100, required=True)
    phone_number = serializers.IntegerField(required=True)


class ListSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=200, required=True)


class UserPhoneSerializer(serializers.Serializer):
    phone_number = serializers.IntegerField(required=False)


class DetailSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    password = serializers.CharField(max_length=200, allow_null=False)
    email = serializers.CharField(max_length=200, allow_null=False)
    first_name = serializers.CharField(max_length=100, required=False)
    phone_number = serializers.SerializerMethodField()

    def get_phone_number(self, obj):
        obj = UserPhone.objects.get(user_detail=obj)
        return UserPhoneSerializer(obj).data

    def to_representation(self, instance):
        data = super().to_representation(instance)
        extra = data['phone_number']
        del data['phone_number']
        data['phone_number'] = extra['phone_number']
        return data


class LoginSerializers(serializers.Serializer):
    email = serializers.CharField(required=True, max_length=200)
    password = serializers.CharField(max_length=200, required=True)