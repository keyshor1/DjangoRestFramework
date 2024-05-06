
from django.contrib import admin
from django.urls import path
from api  import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/student/', views.StudentAPI.as_view()),
    path('api/student/<int:pk>', views.StudentAPI.as_view()),
]
