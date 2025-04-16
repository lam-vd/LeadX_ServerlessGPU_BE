from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

gpu_type_list_response_200 = openapi.Response(
    description="GPU type list retrieved successfully",
    examples={
        "application/json": {
            "data": [
                {"id": 1, "name": "nvidia-tesla-t4", "status": 1},
                {"id": 2, "name": "nvidia-a100", "status": 1},
                {"id": 3, "name": "nvidia-rtx-3090", "status": 1}
            ],
            "message": "gpu_type_list_retrieved_successfully",
            "status": 200
        }
    }
)

gpu_type_list_swagger = swagger_auto_schema(
    operation_summary="Get GPU Type List",
    operation_description="Retrieve a list of available GPU types.",
    responses={200: gpu_type_list_response_200}
)