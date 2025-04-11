from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

# Response schema for 200 OK
task_detail_response_200 = openapi.Response(
    description="Task details retrieved successfully",
    examples={
        "application/json": {
            "data": {
                "id": 1,
                "task_name": "Example Task",
                "description": "This is an example task.",
                "image_path": "https://example.com/image.png",
                "endpoint": "https://example.com/api/task/1",
                "region": "tokyo",
                "source_path": "/path/to/source.py",
                "source_code": "print('Hello, World!')",
                "created_at": "2025-03-27T10:00:00Z",
                "updated_at": "2025-03-27T12:00:00Z",
                "deleted_at": None
            },
            "message": "task_details_retrieved_successfully",
            "status": 200
        }
    }
)

# Response schema for 404 Not Found
task_detail_response_404 = openapi.Response(
    description="Task not found",
    examples={
        "application/json": {
            "errors": {"task_id": "task_not_found"},
            "message": "task_not_found",
            "status": 404
        }
    }
)

# Swagger schema for Get Task Detail API
get_task_swagger_schema = swagger_auto_schema(
    operation_summary="Get Task Details",
    operation_description="Retrieve the details of a specific task by its ID.",
    responses={
        200: task_detail_response_200,
        404: task_detail_response_404,
        500: "Internal Server Error"
    }
)