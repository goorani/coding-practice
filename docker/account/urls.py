from django.urls import path
from . import views


urlpatterns = [
    path('', views.account, name='account'),
    path("health/", views.health_check, name='health'),
]