from django.shortcuts import render
from rest_framework.views import APIView
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
# Create your views here.


def index(request):
    return render(request,'index.html')

def funcname(request):
       student  = Student.objects.all()
       serializer = StudentSerializer(student, many=True)
       return Response(serializer.data)

class StudentView(APIView):

    # def get(self, request):
    #    student  = Student.objects.all()
    #    serializer = StudentSerializer(student, many=True)
    #    return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)


        

        