
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/student/', views.ListCreateAPI.as_view()),
    path('api/student/<int:pk>/', views.RetrieveUpdateDestroyAPI.as_view())
]
