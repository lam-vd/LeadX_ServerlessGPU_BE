from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

delete_job_request_body = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=["job_id"],
    properties={
        "job_id": openapi.Schema(
            type=openapi.TYPE_STRING,
            description="ID of the job to delete",
            example="job-europe-west2-b4ac30a5-9df2-4bd8-a68c-fa94e64d16b1"
        ),
    },
)

delete_job_response_200 = openapi.Response(
    description="Job deleted successfully",
    examples={
        "application/json": {
            "data": {},
            "message": "job_deleted_successfully",
            "status": 200
        }
    }
)

delete_job_response_404 = openapi.Response(
    description="Job not found",
    examples={
        "application/json": {
            "errors": {"job_id": "job_not_found"},
            "message": "job_not_found",
            "status": 404
        }
    }
)

delete_job_swagger = swagger_auto_schema(
    operation_summary="Delete Job",
    operation_description="Delete a specific job by its ID.",
    request_body=delete_job_request_body,
    responses={
        200: delete_job_response_200,
        404: delete_job_response_404,
        500: "Internal Server Error"
    }
)