from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from core.services.gpu_job_service import GPUJobService
from core.models.job import Job
from core.utils.response_formatter import success_response, error_response
from core.swagger.delete_job_swagger import delete_job_swagger
from django.utils import timezone

class DeleteJobView(APIView):
    permission_classes = [IsAuthenticated]

    @delete_job_swagger
    def post(self, request):
        job_id = request.data.get("job_id")
        if not job_id:
            return error_response(
                errors={"job_id": "This field is required."},
                message="validation_error",
                status_code=status.HTTP_400_BAD_REQUEST
            )

        try:
            job = Job.objects.get(job_id=job_id)
            GPUJobService.delete_job(job_id)
            job.deleted_at = timezone.now()
            job.save()

            return success_response(
                data={},
                message="job_deleted_successfully",
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
                message="failed_to_delete_job",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )