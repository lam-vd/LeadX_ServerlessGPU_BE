from rest_framework import serializers
from core.models.task import Task
from core.models.job import Job

class TaskJobListSerializer(serializers.ModelSerializer):
    task_name = serializers.CharField(source="task.task_name")
    gpu_type = serializers.CharField(source="gpu_type.name")
    status = serializers.CharField(source="get_status_display")
    created_at = serializers.DateTimeField()

    class Meta:
        model = Job
        fields = ["task_name", "gpu_type", "status", "created_at"]