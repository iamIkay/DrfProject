from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student
from .serialization import StudentSerializer

# Create your views here.
class TesView(APIView):
    def post(self, request, *args, **kwargs):
        studentSerialized = StudentSerializer(data = request.data)
        if studentSerialized.is_valid():
            studentSerialized.save()
            return Response(studentSerialized.data)
           
    
    def get(self, request, *args, **kwargs):
        qs = Student.objects.all()
        dataSerializer = StudentSerializer(qs, many=True)
        return Response(dataSerializer.data)