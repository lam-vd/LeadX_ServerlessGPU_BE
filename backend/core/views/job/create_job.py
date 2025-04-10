from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from core.serializers.job import CreateJobSerializer
from core.utils.response_formatter import success_response, error_response
from core.swagger.create_job import create_job_swagger

class CreateJobView(APIView):
    permission_classes = [IsAuthenticated]

    @create_job_swagger
    def post(self, request):
        serializer = CreateJobSerializer(data=request.data)
        if serializer.is_valid():
            job = serializer.save()
            return success_response(
                data={"job_id": job.job_id},
                message="job_created_successfully",
                status_code=status.HTTP_201_CREATED
            )
        return error_response(
            errors=serializer.errors,
            message="validation_error",
            status_code=status.HTTP_400_BAD_REQUEST
        )