from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

job_detail_response_200 = openapi.Response(
    description="Job detail retrieved successfully",
    examples={
        "application/json": {
            "data": {
                "task_name": "Train Yolo8 - Facedetetch",
                "gpu_type": "gpu_1x_h200_i",
                "cuda": "CUDA-enabled Quadro",
                "start_time": "2025-01-06T08:03:00Z",
                "end_time": "2025-01-06T18:03:00Z",
                "total_time": "10h",
                "status": "Completed",
                "total_fee": "$50.00"
            },
            "message": "job_detail_retrieved_successfully",
            "status": 200
        }
    }
)

job_detail_response_404 = openapi.Response(
    description="Job not found",
    examples={
        "application/json": {
            "errors": {"job_id": "Job not found."},
            "message": "job_not_found",
            "status": 404
        }
    }
)

job_detail_swagger = swagger_auto_schema(
    operation_summary="Get Job Detail",
    operation_description="Retrieve the details of a specific job by its ID.",
    responses={
        200: job_detail_response_200,
        404: job_detail_response_404,
        500: "Internal Server Error"
    }
)