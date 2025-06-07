from rest_framework import serializers
from core.models.task import Task

class TaskSerializer(serializers.ModelSerializer):
    source_code = serializers.CharField(write_only=True)
    run_count = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = [
          "id",
          "task_name",
          "description",
          "source_code",
          "endpoint",
          "run_count",
          "created_at",
          "updated_at",
          "deleted_at",
        ]

    def get_run_count(self, obj):
        return obj.job_set.count() if hasattr(obj, 'job_set') else 0