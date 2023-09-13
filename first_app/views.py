from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def employeeView(request):
    emp = {
        'id': 123,
        'name': 'John',
        'sal': 1000_000,
    }

    return JsonResponse(emp)    # Serializes the dictionary to json
