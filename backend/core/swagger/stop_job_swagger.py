from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

stop_job_request_body = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=["job_id"],
    properties={
        "job_id": openapi.Schema(
            type=openapi.TYPE_STRING,
            description="ID of the job to stop",
            example="job-europe-west2-b4ac30a5-9df2-4bd8-a68c-fa94e64d16b1"
        ),
    },
)

stop_job_response_200 = openapi.Response(
    description="Job stopped successfully",
    examples={
        "application/json": {
            "data": {"job_id": "job-europe-west2-b4ac30a5-9df2-4bd8-a68c-fa94e64d16b1", "status": "Stopped"},
            "message": "job_stopped_successfully",
            "status": 200
        }
    }
)

stop_job_response_404 = openapi.Response(
    description="Job not found",
    examples={
        "application/json": {
            "errors": {"job_id": "job_not_found"},
            "message": "job_not_found",
            "status": 404
        }
    }
)

stop_job_swagger = swagger_auto_schema(
    operation_summary="Stop Job",
    operation_description="Stop a specific job by its ID.",
    request_body=stop_job_request_body,
    responses={
        200: stop_job_response_200,
        404: stop_job_response_404,
        500: "Internal Server Error"
    }
)