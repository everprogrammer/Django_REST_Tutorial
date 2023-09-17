from rest_framework import viewsets
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination


# create your views here
# Supports primary and non-primary key based restful endpoints
class EmployeePagination(PageNumberPagination):
    page_size = 1

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = EmployeePagination # this class overrides the default in settings


