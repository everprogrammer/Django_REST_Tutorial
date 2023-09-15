from django.urls import path
from .import views

urlpatterns = [
    path('emps/', views.employeeView),
    path('employees/', views.employee_list),
    path('employees/<int:pk>', views.employee_detail),

]