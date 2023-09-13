from django.shortcuts import render
from django.http import JsonResponse
from .models import Employee

# Create your views here.
def employeeView(request):
    
    data = Employee.objects.all() # it's a queryset, now we need a dictionary
    response = {'employees': list(data.values('name', 'sal'))}

    return JsonResponse(response)    # Serializes the dictionary to json
