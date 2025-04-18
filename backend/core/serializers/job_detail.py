from rest_framework import serializers
from core.models.job import Job

class JobDetailSerializer(serializers.ModelSerializer):
    task_name = serializers.CharField(source="task.task_name")
    gpu_type = serializers.CharField(source="gpu_type.name")
    cuda = serializers.SerializerMethodField()
    total_time = serializers.SerializerMethodField()
    total_fee = serializers.SerializerMethodField()

    class Meta:
        model = Job
        fields = [
            "task_name",
            "gpu_type",
            "cuda",
            "start_time",
            "end_time",
            "total_time",
            "status",
            "total_fee",
        ]

    def get_cuda(self, obj):
        return "CUDA-enabled Quadro" if obj.gpu_type else "Unknown"

    def get_total_time(self, obj):
        if obj.start_time and obj.end_time:
            total_seconds = (obj.end_time - obj.start_time).total_seconds()
            hours = total_seconds // 3600
            return f"{int(hours)}h"
        return "N/A"

    def get_total_fee(self, obj):
        hourly_rate = 5
        if obj.start_time and obj.end_time:
            total_seconds = (obj.end_time - obj.start_time).total_seconds()
            hours = total_seconds / 3600
            return f"${hours * hourly_rate:.2f}"
        return "$0.00"