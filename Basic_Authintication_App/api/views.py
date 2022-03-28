from Basic_Authintication_App.models import EmployeeData
from Basic_Authintication_App.api.serializers import EmplyeeDataSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated





class Employee_Model_View(viewsets.ModelViewSet):
    query_set = EmployeeData.objects.all()
    serializer_class = EmplyeeDataSerializer

    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

