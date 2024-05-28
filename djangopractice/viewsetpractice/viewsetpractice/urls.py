from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views
# Create your views here.

router = DefaultRouter()

router.register('viewstudapi', views.StudentReadOnlyView, basename='studentview')


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
]
