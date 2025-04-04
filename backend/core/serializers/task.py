from rest_framework import serializers
from core.models.task import Task

class TaskSerializer(serializers.ModelSerializer):
    source_code = serializers.CharField(write_only=True)

    class Meta:
        model = Task
        fields = ["task_name", "description", "source_code"]