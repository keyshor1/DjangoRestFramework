from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from  rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def StudentView(request, pk=None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            student = Student.objects.get(id=id)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)
        
    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data is created', 'context': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    if request.method == 'PUT':
        studentid = Student.objects.get(id=pk)
        serializer = StudentSerializer(studentid, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Useris fully Updated', 'context': serializer.data}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PATCH':
        studentid = Student.objects.get(id=pk)
        serializer = StudentSerializer(studentid, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Useris partially Updated', 'context': serializer.data}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        student = Student.objects.get(id=pk)
        student.delete()
        return Response({'msg': 'Data is deleted successfully'}, status=status.HTTP_202_ACCEPTED)