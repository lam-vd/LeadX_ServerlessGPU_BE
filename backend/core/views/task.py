from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from core.serializers.task import TaskSerializer
from core.services.task_service import TaskService
from core.models.task import Task
from core.utils.response_formatter import success_response, error_response
from core.validators.source_code_validator import validate_source_code
from core.swagger.create_task_swagger import create_task_swagger
import logging

logger = logging.getLogger(__name__)

class CreateTaskView(APIView):
    permission_classes = [IsAuthenticated]

    @create_task_swagger
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            task_name = serializer.validated_data["task_name"]
            description = serializer.validated_data["description"]
            source_code = serializer.validated_data["source_code"]

            try:
                validate_source_code(source_code)
                file_path = self._save_source_code(user, source_code)
                image_path = self._build_image(user, task_name, file_path)
                task = self._create_task(user, task_name, description, file_path, image_path)
                return success_response(
                    data={
                        "task_id": task.id,
                        "task_name": task.task_name,
                        "description": task.description,
                        "image_path": task.image_path,
                    },
                    message="task_created_successfully",
                    status_code=status.HTTP_201_CREATED,
                )
            except Exception as e:
                logger.error(f"Failed to create task: {str(e)}")
                return error_response(
                    errors={"error": str(e)},
                    message="failed_to_create_task",
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )

        return error_response(
            errors=serializer.errors,
            message="validation_errors",
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    def _save_source_code(self, user, source_code):
        return TaskService.save_source_code(user, source_code)

    def _build_image(self, user, task_name, file_path):
        TaskService.create_dockerfile(file_path)
        return TaskService.build_and_push_image(user, task_name, file_path)

    def _create_task(self, user, task_name, description, file_path, image_path):
        return Task.objects.create(
            user=user,
            task_name=task_name,
            description=description,
            source_path=file_path,
            image_path=image_path,
        )