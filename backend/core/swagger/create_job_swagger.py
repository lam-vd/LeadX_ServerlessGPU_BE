from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

# Request body schema
create_job_request_body = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=["task_name", "gpu_type"],
    properties={
        "task_name": openapi.Schema(
            type=openapi.TYPE_STRING,
            description="Name of the task for which the job is being created",
            example="Train Yolo8 - Treedetech"
        ),
        "gpu_type": openapi.Schema(
            type=openapi.TYPE_STRING,
            description="Type of GPU to use for the job",
            example="nvidia-tesla-t4"
        ),
    },
)

# Response schema for 201 Created
create_job_response_201 = openapi.Response(
    description="Job created successfully",
    examples={
        "application/json": {
            "data": {"job_id": "job-12345"},
            "message": "job_created_successfully",
            "status": 201
        }
    }
)

# Response schema for 400 Bad Request
create_job_response_400 = openapi.Response(
    description="Validation error",
    examples={
        "application/json": {
            "errors": {"task_name": "Task not found or does not belong to the user"},
            "message": "validation_error",
            "status": 400
        }
    }
)

# Swagger schema for Create Job API
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