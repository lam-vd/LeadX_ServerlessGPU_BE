from rest_framework import serializers
from core.models.gpu_type import GpuType

class GpuTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GpuType
        fields = ["id", "name", "status"]