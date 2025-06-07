from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

delete_task_response_200 = openapi.Response(
    description="Task deleted successfully",
    examples={
        "application/json": {
            "data": {},
            "message": "task_deleted_successfully",
            "status": 200
        }
    }
)

delete_task_response_404 = openapi.Response(
    description="Task not found",
    examples={
        "application/json": {
            "errors": {"task_id": "task_not_found"},
            "message": "task_not_found",
            "status": 404
        }
    }
)

delete_task_swagger = swagger_auto_schema(
    operation_summary="Delete Task",
    operation_description="Delete a specific task by its ID.",
    responses={
        200: delete_task_response_200,
        404: delete_task_response_404,
        500: "Internal Server Error"
    }
)