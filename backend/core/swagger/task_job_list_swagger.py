from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

# Enum cho status
STATUS_CHOICES = ["pending", "running", "completed", "failed", "stopped"]

task_job_list_query_params = [
    openapi.Parameter(
        "status",
        openapi.IN_QUERY,
        description="Job status (Pending, Running, Completed, Failed, Stopped)",
        type=openapi.TYPE_STRING,
        enum=STATUS_CHOICES,
    ),
    openapi.Parameter(
        "gpu_type",
        openapi.IN_QUERY,
        description="GPU type",
        type=openapi.TYPE_STRING,
    ),
    openapi.Parameter(
        "task_name",
        openapi.IN_QUERY,
        description="Task name",
        type=openapi.TYPE_STRING,
    ),
    openapi.Parameter(
        "start_date",
        openapi.IN_QUERY,
        description="Start date (yyyy-mm-dd)",
        type=openapi.TYPE_STRING,
    ),
    openapi.Parameter(
        "end_date",
        openapi.IN_QUERY,
        description="End date (yyyy-mm-dd)",
        type=openapi.TYPE_STRING,
    ),
    openapi.Parameter(
        "page",
        openapi.IN_QUERY,
        description="Page number",
        type=openapi.TYPE_INTEGER,
    ),
    openapi.Parameter(
        "page_size",
        openapi.IN_QUERY,
        description="Number of items per page",
        type=openapi.TYPE_INTEGER,
    ),
]

task_job_list_response_200 = openapi.Response(
    description="Task and Job list retrieved successfully",
    examples={
        "application/json": {
            "data": {
                "results": [
                    {
                        "task_name": "Train Yolo8 - Treedetech",
                        "gpu_type": "gpu_1x_h200_i",
                        "status": "Pending",
                        "created_at": "2023-10-01T10:00:00Z",
                    },
                    {
                        "task_name": "Train Yolo8 - Treedetech",
                        "gpu_type": "gpu_1x_h200_i",
                        "status": "Running",
                        "created_at": "2023-10-01T11:00:00Z",
                    },
                ],
                "count": 50,
                "next": "http://127.0.0.1:8000/api/task-job-list/?page=2",
                "previous": None,
            },
            "status": 200,
            "message": "task_job_list_retrieved_successfully",
        }
    },
)

swagger_task_job_list = swagger_auto_schema(
    operation_summary="Get Task and Job List",
    operation_description="Retrieve a paginated list of tasks and jobs with filters for status, GPU type, and task name.",
    manual_parameters=task_job_list_query_params,
    responses={200: task_job_list_response_200},
)