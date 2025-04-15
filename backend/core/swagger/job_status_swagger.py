from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

# Path parameter schema
job_status_path_param = [
    openapi.Parameter(
        "job_id",
        openapi.IN_PATH,
        description="ID of the job to check status",
        type=openapi.TYPE_STRING,
        required=True,
        example="job-12345"
    )
]

# Response schema for 200 OK
job_status_response_200 = openapi.Response(
    description="Job status retrieved successfully",
    examples={
        "application/json": {
            "data": {"status": "Running"},
            "message": "job_status_retrieved_successfully",
            "status": 200
        }
    }
)

# Response schema for 404 Not Found
job_status_response_404 = openapi.Response(
    description="Job not found",
    examples={
        "application/json": {
            "errors": {"job_id": "job_not_found"},
            "message": "job_not_found",
            "status": 404
        }
    }
)

# Swagger schema for Get Job Status API
get_job_status_swagger = swagger_auto_schema(
    operation_summary="Get Job Status",
    operation_description="Retrieve the status of a specific job by its ID.",
    manual_parameters=job_status_path_param,
    responses={
        200: job_status_response_200,
        404: job_status_response_404,
        500: "Internal Server Error"
    }
)