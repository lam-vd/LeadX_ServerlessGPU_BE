from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

create_job_request_body = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=["task_id", "gpu_type"],
    properties={
        "task_id": openapi.Schema(
            type=openapi.TYPE_INTEGER,
            description="ID of the task",
            example=1
        ),
        "gpu_type": openapi.Schema(
            type=openapi.TYPE_STRING,
            description="Type of GPU to use",
            example="nvidia-tesla-t4"
        ),
    },
)

create_job_response_201 = openapi.Response(
    description="Job created successfully",
    examples={
        "application/json": {
            "data": {"job_id": "job-1-nvidia-tesla-t4"},
            "message": "job_created_successfully",
            "status": 201
        }
    }
)

create_job_response_400 = openapi.Response(
    description="Validation error",
    examples={
        "application/json": {
            "errors": {"task_id": ["Task not found."]},
            "message": "validation_error",
            "status": 400
        }
    }
)

create_job_swagger = swagger_auto_schema(
    operation_summary="Create Job",
    operation_description="Create a new job for a specific task and GPU type.",
    request_body=create_job_request_body,
    responses={
        201: create_job_response_201,
        400: create_job_response_400,
        500: "Internal Server Error"
    }
)