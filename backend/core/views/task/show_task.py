from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from core.models.task import Task
from core.serializers.detail_task import TaskDetailSerializer
from core.utils.response_formatter import success_response, error_response
from core.swagger.show_task_swagger import get_task_swagger_schema

class GetTaskDetailView(APIView):
    permission_classes = [IsAuthenticated]

    @get_task_swagger_schema
    def get(self, request, task_id):
        try:
            task = Task.objects.get(id=task_id, user=request.user, deleted_at__isnull=True)
            serializer = TaskDetailSerializer(task)
            return success_response(
                data=serializer.data,
                message="task_details_retrieved_successfully",
                status_code=status.HTTP_200_OK
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