from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializer import StudentSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissionsOrAnonReadOnly, AllowAny, IsAdminUser

class StudentAPI(APIView):
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    
    # for session authentication we have make changes add urls.py
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAdminUser]
    

    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            studentdata = Student.objects.get(id=id)
            serializer = StudentSerializer(studentdata, )
            return Response(serializer.data)
        studentdata = Student.objects.all()
        serializer = StudentSerializer(studentdata, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        data = request.data
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            context = {'msg': "User is Created"}
            return Response(context, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, format=None):
        id = pk
        studentid = Student.objects.get(id=id)
        serializer = StudentSerializer(studentid, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'user is fully updated'}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def patch(self, request, pk, format=None):
        id = pk
        data = request.data
        studentid = Student.objects.get(id=id)
        serializer = StudentSerializer(studentid, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'user is partially updated'}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        studentid = Student.objects.get(id=pk)
        studentid.delete()
        return Response({'msg': 'user is deleted'}, status=status.HTTP_204_NO_CONTENT)
