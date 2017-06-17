from tastypie.resources import ModelResource
from api.models import Employee


class EmployeeResource(ModelResource):
    class Meta:
        queryset = Employee.objects.all()
        resource_name = 'employee'
