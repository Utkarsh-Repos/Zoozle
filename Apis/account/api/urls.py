from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('accountapi', views.AccountCreation, basename='accountapi')

urlpatterns = [
    path('', include(router.urls)),
    path('detail/', views.DetailData.as_view()),
    path('login/', views.LoginApi.as_view()),
]