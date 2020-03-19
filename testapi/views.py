from django.shortcuts import render, redirect
from rest_framework.views import APIView
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from django.views.generic import View
# from .tasks import api_order_home_success
# Create your views here.
from .vpn import get_student_url, request_get

class IndexView(View):

    def get(self, request):
        # ten = request.GET['hoten']
        # tuoi = request.GET['tuoi']
        # gioitinh = request.GET['gioitinh']
        # print(ten)
        # print(gioitinh)
        # print(tuoi)
        print('*********************************************')
        # print(request.GET)
        data = {'csrfmiddlewaretoken': 'rK9AAwy9NZWdtQ7oFrRPSnBqYjkIBElbqjLsARYukLLSoZIPOPAXTOZ3oHSyUOlw', 'hoten': 'nguyen van a', 'tuoi': '23', 'gioitinh': 'nam'}
        url = get_student_url(data)
        print(url)
        request_get(url)
        # api_order_home_success(name,tuoi,gioitinh)
        return render(request,'index.html')

    # def post(self, request):
    #     name = request.POST['hoten']
    #     tuoi = request.POST['tuoi']
    #     gioitinh = request.POST['gioitinh']
    #     print(tuoi)
    #     api_order_home_success(name,tuoi,gioitinh)
    #     return redirect('index')


class StudentView(APIView):

    def get(self, request):
       student  = Student.objects.all()
       serializer = StudentSerializer(student, many=True)
       return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        request.session['hoten']=request.data['hoten']
        request.session['tuoi'] = request.data['tuoi']
        request.session['gioitinh']=request.data['gioitinh']
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else :
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# class CallAPI(APIView):
#     def post(self, request):
#         name = request.session.get('hoten')
#         student = Student.objects.filter(hoten=name)
#         if student:
#             serializer = StudentSerializer(data=student)
            
