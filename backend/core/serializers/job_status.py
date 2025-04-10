from rest_framework import serializers

class JobStatusSerializer(serializers.Serializer):
    job_id = serializers.CharField(required=True)