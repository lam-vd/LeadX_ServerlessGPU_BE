from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from core.serializers.task import TaskSerializer

create_task_request_body = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=["task_name", "source_code"],
    properties={
        "task_name": openapi.Schema(
            type=openapi.TYPE_STRING,
            description="Name of the task",
            example="Example Task"
        ),
        "description": openapi.Schema(
            type=openapi.TYPE_STRING,
            description="Description of the task (optional)",
            example="This is an example task"
        ),
        "source_code": openapi.Schema(
            type=openapi.TYPE_STRING,
            description="Python source code as a string",
            example="print('Hello, World!')"
        ),
    },
)

create_task_response_201 = openapi.Response(
    description="Task created successfully",
    examples={
        "application/json": {
            "task_id": 1,
            "task_name": "Example Task",
            "description": "This is an example task",
            "image_path": "123.456.789.10:5000/user_6b86b273ff_example_task:latest"
        }
    }
)

create_task_response_400 = openapi.Response(
    description="Validation error",
    examples={
        "application/json": {
            "errors": {
                "task_name": ["This field is required."],
                "source_code": ["This field is required."]
            },
            "message": "validation_errors",
            "status": 400
        }
    }
)

create_task_response_500 = openapi.Response(
    description="Failed to create task",
    examples={
        "application/json": {
            "errors": {
                "error": "Failed to build Docker image"
            },
            "message": "failed_to_create_task",
            "status": 500
        }
    }
)

create_task_swagger = swagger_auto_schema(
    operation_summary="Create Task",
    operation_description="Create a new task by uploading Python source code and building a Docker image.",
    request_body=create_task_request_body,
    responses={
        201: create_task_response_201,
        400: create_task_response_400,
        500: create_task_response_500,
    }
)