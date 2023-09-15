from rest_framework import viewsets
from .models import Employee
from .serializers import EmployeeSerializer


# create your views here
# Supports primary and non-primary key based restful endpoints
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
