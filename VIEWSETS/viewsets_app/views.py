from rest_framework import viewsets
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# create your views here
# Supports primary and non-primary key based restful endpoints
class EmployeePagination(PageNumberPagination):
    page_size = 3

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = EmployeePagination # this class overrides the default in settings
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['name', 'sal']

    ## Search filter
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['^id', '^name'] ## starts with search word
                                    ## '=name' > search word is exactly the name

    ## OrderingFilter
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['name', 'sal']

    

