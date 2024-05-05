from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from .serializers import StudentSerializer
import io
from django.views.decorators.csrf import csrf_exempt
from .models import Student
from django.views import View
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class student_crud(View):
    def get(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        if id is not None:
            studentdata = Student.objects.get(id=id)
            serializer = StudentSerializer(studentdata) 
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
        
        studentdata = Student.objects.all()
        serializer = StudentSerializer(studentdata, many=True)
        json_data = JSONRenderer().render(serializer._data)
        return HttpResponse(json_data, content_type='application/json')
    
    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            success = {'success': "Data is added successfully "}
            json_data = JSONRenderer().render(success)
            return HttpResponse(json_data, content_type='application/json')
        return JsonResponse(serializer.errors)

    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        # retrieve id from frontend
        id = python_data.get('id')
        # check the id with the database of model student 
        studentid = Student.objects.get(id=id)
        serializer = StudentSerializer(studentid, data=python_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            success = {'success': "Data is updated successfully "}
            json_data = JSONRenderer().render(success)
            return HttpResponse(json_data, content_type='application/json')
        return JsonResponse(serializer.errors)


    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        student = Student.objects.get(id=id)
        student.delete()
        context = {'msg': 'deleted successfully'}
        return JsonResponse(context, safe=False)










def student_detail(request):
    student = Student.objects.all()
    serializer = StudentSerializer(student, many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data)

def student_individual(request, pk):
    student = Student.objects.get(id=pk)
    serializer = StudentSerializer(student)
    return JsonResponse(serializer.data)

# Create your views here.
@csrf_exempt
def student_create(request):
     if request.method == 'POST':
        json_data = request.body
        # convert json data to stream and then to python nativesdatatype
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        # serialize python nativedata
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            context = {'msg': 'Data is created'}
            # now again pass this context dictinary or serialized data to json data
            json_data = JSONRenderer().render(context)
            return HttpResponse(json_data, content_type='application/json')

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')


