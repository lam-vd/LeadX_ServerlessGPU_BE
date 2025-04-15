from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

job_status_query_param = [
    openapi.Parameter(
        "job_id",
        openapi.IN_QUERY,
        description="ID of the job to check status",
        type=openapi.TYPE_STRING,
        required=True,
        example="job-europe-west2-b4ac30a5-9df2-4bd8-a68c-fa94e64d16b1"
    )
]

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

job_status_response_400 = openapi.Response(
    description="Validation error or failed to fetch job status",
    examples={
        "application/json": {
            "errors": {"error": "Job ID not found."},
            "message": "failed_to_fetch_job_status",
            "status": 400
        }
    }
)

job_status_swagger = swagger_auto_schema(
    operation_summary="Get Job Status",
    operation_description="Retrieve the status of a specific job by its ID.",
    manual_parameters=job_status_query_param,
    responses={
        200: job_status_response_200,
        400: job_status_response_400,
        500: "Internal Server Error"
    }
)