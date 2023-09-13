from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Employee
from .seializers import EmployeeSerializer

# Create your views here.
def employeeView(request):
    data = Employee.objects.all() # it's a queryset, now we need a dictionary
    response = {'employees': list(data.values('name', 'sal'))}

    return JsonResponse(response)    # Serializes the dictionary to json


@api_view(['GET', 'POST'])
def employee_list(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        # first de-serialize the data
        serializer = EmployeeSerializer(data=request.data)
        # validate the serializer
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



