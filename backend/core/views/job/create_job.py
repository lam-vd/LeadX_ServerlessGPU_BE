from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from core.services.gpu_job_service import GPUJobService
from core.models.job import Job
from core.models.task import Task
from core.utils.response_formatter import success_response, error_response
from core.swagger.create_job_swagger import create_job_swagger

class CreateJobView(APIView):
    permission_classes = [IsAuthenticated]

    @create_job_swagger
    def post(self, request):
        task_name = request.data.get("task_name")
        gpu_type = request.data.get("gpu_type")

        if not task_name or not gpu_type:
            return error_response(
                errors={"detail": "task_name and gpu_type are required"},
                message="validation_error",
                status_code=status.HTTP_400_BAD_REQUEST
            )

        try:
            task = Task.objects.filter(task_name=task_name, user=request.user, deleted_at__isnull=True).first()
            if not task:
                return error_response(
                    errors={"task_name": "Task not found or does not belong to the user"},
                    message="task_not_found",
                    status_code=status.HTTP_404_NOT_FOUND
                )

            gpu_response = GPUJobService.create_job(gpu_type, task.image_path)
            job_id = gpu_response.get("job_id")

            Job.objects.create(
                task=task,
                job_id=job_id,
                status=0,  # Pending
                gpu_type_id=gpu_type
            )

            return success_response(
                data={"job_id": job_id},
                message="job_created_successfully",
                status_code=status.HTTP_201_CREATED
            )
        except Exception as e:
            return error_response(
                errors={"error": str(e)},
                message="failed_to_create_job",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )