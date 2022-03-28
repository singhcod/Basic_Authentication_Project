from Basic_Authintication_App.models import EmployeeData
from rest_framework import serializers

class EmplyeeDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeData
        fields = "__all__"