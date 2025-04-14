from rest_framework import serializers
from core.models.task import Task
import os

class TaskDetailSerializer(serializers.ModelSerializer):
    source_code = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = [
            "id",
            "task_name",
            "description",
            "image_path",
            "endpoint",
            "source_path",
            "source_code",
            "created_at",
            "updated_at",
            "deleted_at",
        ]

    def get_source_code(self, obj):
        if obj.source_path and os.path.exists(obj.source_path):
            try:
                with open(obj.source_path, "r") as file:
                    return file.read()
            except Exception as e:
                return f"Error reading source file: {str(e)}"
        return None