from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from core.models.task import Task
from core.serializers.task import TaskSerializer
from core.utils.response_formatter import success_response, error_response
from core.swagger.edit_task_swagger import edit_task_swagger

class EditTaskView(APIView):
    permission_classes = [IsAuthenticated]

    @edit_task_swagger
    def put(self, request, task_id):
        try:
            task = Task.objects.get(id=task_id, user=request.user, deleted_at__isnull=True)
            serializer = TaskSerializer(task, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return success_response(
                    data=serializer.data,
                    message="task_updated_successfully",
                    status_code=status.HTTP_200_OK
                )
            return error_response(
                errors=serializer.errors,
                message="validation_error",
                status_code=status.HTTP_400_BAD_REQUEST
            )
        except Task.DoesNotExist:
            return error_response(
                errors={"task_id": "task_not_found"},
                message="task_not_found",
                status_code=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return error_response(
                errors={"error": str(e)},
                message="an_unexpected_error_occurred",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )