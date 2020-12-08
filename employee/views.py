from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Employee
from .serializers import ArticleSerializer


class ArticleView(APIView):
    
    def get(self, request):
        """
        """"

        employee = Employee.objects.all()
        serializer = EmployeeSerializer(articles, many=True)
        return Response({"employee": serializer.data})


    def post(self, request):
        """
        """

        employee = request.data.get('employee')        
        serializer = EmployeeSerializer(data=employee)
        if serializer.is_valid(raise_exception=True):
            employee_saved = serializer.save()
        return Response({"success": "Employee '{}' added successfully".format(employee_saved.first_name + employee_saved.last_name)})