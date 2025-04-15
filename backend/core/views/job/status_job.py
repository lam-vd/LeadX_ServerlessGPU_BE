from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from core.serializers.job_status import JobStatusSerializer
from core.utils.response_formatter import success_response, error_response
from core.swagger.status_job import job_status_swagger
from django.conf import settings
import requests

class JobStatusView(APIView):
    permission_classes = [IsAuthenticated]

    @job_status_swagger
    def get(self, request):
        serializer = JobStatusSerializer(data=request.query_params)
        if serializer.is_valid():
            job_id = serializer.validated_data["job_id"]
            api_url = f"{settings.GPU_SERVERLESS_API_BASE_URL}/job/status?job_id={job_id}"
            try:
                response = requests.get(api_url, headers={"accept": "application/json"})
                response_data = response.json()

                if response.status_code != 200:
                    return error_response(
                        errors={"error": response_data.get("message", "Failed to fetch job status.")},
                        message="failed_to_fetch_job_status",
                        status_code=status.HTTP_400_BAD_REQUEST
                    )

                return success_response(
                    data={"status": response_data.get("status")},
                    message="job_status_retrieved_successfully",
                    status_code=status.HTTP_200_OK
                )
            except requests.RequestException as e:
                return error_response(
                    errors={"error": f"Failed to connect to GPU server: {str(e)}"},
                    message="failed_to_fetch_job_status",
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

        return error_response(
            errors=serializer.errors,
            message="validation_error",
            status_code=status.HTTP_400_BAD_REQUEST
        )