"""URL mappings for prispevok app"""
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from prispevok import views


router = DefaultRouter()
router.register('prispevoks', views.PrispevokViewSet)

app_name = 'prispevok'

urlpatterns = [
    path('', include(router.urls))
]
