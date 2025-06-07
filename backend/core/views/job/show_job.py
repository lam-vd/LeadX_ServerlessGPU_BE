from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from core.models.job import Job
from core.serializers.job_detail import JobDetailSerializer
from core.utils.response_formatter import success_response, error_response
from core.swagger.show_job_swagger import job_detail_swagger
class JobDetailView(APIView):
    permission_classes = [IsAuthenticated]

    @job_detail_swagger
    def get(self, request, job_id):
        try:
            job = Job.objects.get(job_id=job_id, deleted_at__isnull=True)
            serializer = JobDetailSerializer(job)
            return success_response(
                data=serializer.data,
                message="job_detail_retrieved_successfully",
                status_code=status.HTTP_200_OK
            )
        except Job.DoesNotExist:
            return error_response(
                errors={"job_id": "Job not found."},
                message="job_not_found",
                status_code=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return error_response(
                errors={"error": str(e)},
                message="failed_to_retrieve_job_detail",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )