from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task  # model we want to serialize
        fields = '__all__'  # field of model we want to show
