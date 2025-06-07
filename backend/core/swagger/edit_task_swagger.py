from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

edit_task_request_body = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "task_name": openapi.Schema(
            type=openapi.TYPE_STRING,
            description="Name of the task",
            example="Updated Task Name"
        ),
        "endpoint": openapi.Schema(
            type=openapi.TYPE_STRING,
            description="Endpoint of the task",
            example="https://example.com/api/task/1"
        ),
        "description": openapi.Schema(
            type=openapi.TYPE_STRING,
            description="Description of the task",
            example="This is an updated description of the task."
        ),
        "source_code": openapi.Schema(
            type=openapi.TYPE_STRING,
            description="Python source code of the task",
            example="print('Updated source code')"
        ),
    }
)

edit_task_response_200 = openapi.Response(
    description="Task updated successfully",
    examples={
        "application/json": {
            "data": {
                "id": 1,
                "task_name": "Updated Task Name",
                "description": "This is an updated description of the task.",
                "endpoint": "https://example.com/api/task/1",
                "run_count": 0,
                "created_at": "2025-03-27T10:00:00Z",
                "updated_at": "2025-03-27T12:00:00Z",
                "deleted_at": None
            },
            "message": "task_updated_successfully",
            "status": 200
        }
    }
)

edit_task_response_400 = openapi.Response(
    description="Validation error",
    examples={
        "application/json": {
            "errors": {
                "task_name": ["This field is required."]
            },
            "message": "validation_error",
            "status": 400
        }
    }
)

edit_task_swagger = swagger_auto_schema(
    operation_summary="Edit Task",
    operation_description="Edit a specific task by its ID. Only the fields `task_name`, `endpoint`, `description`, and `source_code` can be updated.",
    request_body=edit_task_request_body,
    responses={
        200: edit_task_response_200,
        400: edit_task_response_400,
        404: "Task not found",
        500: "Internal Server Error"
    }
)