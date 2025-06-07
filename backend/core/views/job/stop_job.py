from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from core.services.gpu_job_service import GPUJobService
from core.models.job import Job
from core.utils.response_formatter import success_response, error_response
from core.swagger.stop_job_swagger import stop_job_swagger
from django.utils import timezone

class StopJobView(APIView):
    permission_classes = [IsAuthenticated]

    @stop_job_swagger
    def post(self, request):
        job_id = request.data.get("job_id")
        if not job_id:
            return error_response(
                errors={"job_id": "This field is required."},
                message="validation_error",
                status_code=status.HTTP_400_BAD_REQUEST
            )

        try:
            job = Job.objects.get(job_id=job_id, deleted_at__isnull=True)
            if job.status not in [Job.Status.PENDING, Job.Status.RUNNING]:
                return error_response(
                    errors={"job_id": "Job cannot be stopped in its current state."},
                    message="invalid_job_status",
                    status_code=status.HTTP_400_BAD_REQUEST
                )
            GPUJobService.delete_job(job_id)
            job.end_time = timezone.now()
            job.status = Job.Status.STOPPED
            job.total_time = (job.end_time - job.start_time).total_seconds()
            job.save()

            return success_response(
                data={},
                message="job_stopped_successfully",
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
                message="failed_to_stopped_job",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )