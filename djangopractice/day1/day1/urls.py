from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/createstudent/', views.student_create),
    path('api/studentdetail/', views.student_detail),
    path('api/studentdetail/<int:pk>/', views.student_individual),
    path('api/studentcrud/', views.student_crud.as_view()),
]
