from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from core.services.gpu_job_service import GPUJobService
from core.models.job import Job
from core.utils.response_formatter import success_response, error_response
from core.swagger.job_status_swagger import get_job_status_swagger


class GetJobStatusView(APIView):
    permission_classes = [IsAuthenticated]

    @get_job_status_swagger
    def get(self, request, job_id):
        if not job_id:
            return error_response(
                errors={"job_id": "This field is required."},
                message="validation_error",
                status_code=status.HTTP_400_BAD_REQUEST
            )

        try:
            gpu_response = GPUJobService.get_job_status(job_id)
            status = gpu_response.get("status")

            job = Job.objects.get(job_id=job_id)
            job.status = status
            job.save()

            return success_response(
                data={"status": status},
                message="job_status_retrieved_successfully",
                status_code=status.HTTP_200_OK
            )
        except Job.DoesNotExist:
            return error_response(
                errors={"job_id": "job_not_found"},
                message="job_not_found",
                status_code=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return error_response(
                errors={"error": str(e)},
                message="failed_to_get_job_status",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )