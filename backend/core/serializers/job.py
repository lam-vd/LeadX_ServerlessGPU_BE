from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from core.models.job import Job
from core.models.task import Task
from core.models.gpu_type import GpuType
from django.utils import timezone
from django.conf import settings
import requests

class CreateJobSerializer(serializers.ModelSerializer):
    task_id = serializers.IntegerField(write_only=True)
    gpu_type = serializers.CharField(write_only=True)
    job_id = serializers.CharField(read_only=True)

    class Meta:
        model = Job
        fields = ["task_id", "gpu_type", "job_id", "status", "created_at", "updated_at"]

    def validate(self, data):
        # Validate task existence
        try:
            task = Task.objects.get(id=data["task_id"], deleted_at__isnull=True)
            data["task"] = task
        except Task.DoesNotExist:
            raise serializers.ValidationError({"task_id": "Task not found."})

        # Validate GPU type existence
        try:
            gpu_type = GpuType.objects.get(name=data["gpu_type"])
            data["gpu_type"] = gpu_type
        except GpuType.DoesNotExist:
            raise serializers.ValidationError({"gpu_type": "GPU type not found."})

        return data

    def create(self, validated_data):
        api_url = f"{settings.GPU_SERVERLESS_API_BASE_URL}/job/run"
        payload = {
            "gpu_type": validated_data["gpu_type"].name,
            "image_path": validated_data["task"].image_path
        }
        try:
            response = requests.post(api_url, json=payload, headers={"accept": "application/json", "Content-Type": "application/json"})
            response_data = response.json()

            if response.status_code != 202:
                raise ValidationError({"error": response_data.get("message", "Failed to create job on GPU server.")})

            job_id = response_data.get("job_id")
            if not job_id:
                raise ValidationError({"error": "Job ID not returned from GPU server."})

            job = Job.objects.create(
                task=validated_data["task"],
                gpu_type=validated_data["gpu_type"],
                job_id=job_id,
                status=0,  # Pending
                start_time=timezone.now()
            )
            return job

        except requests.RequestException as e:
            raise ValidationError({"error": f"Failed to connect to GPU server: {str(e)}"})