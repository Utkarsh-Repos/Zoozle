from django.contrib import admin
from .models import UserPhone


class UserPhoneAdmin(admin.ModelAdmin):
    class Meta:
        model = UserPhone
        fields = '__all__'


admin.site.register(UserPhone,UserPhoneAdmin)