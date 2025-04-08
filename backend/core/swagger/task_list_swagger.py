from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

task_list_swagger = swagger_auto_schema(
    operation_summary="Get task list",
    operation_description="Retrieve a list of tasks for the current user, including run count and other details.",
    responses={
        200: openapi.Response(
            description="Success",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'count': openapi.Schema(type=openapi.TYPE_INTEGER),
                    'results': openapi.Schema(
                        type=openapi.TYPE_ARRAY,
                        items=openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                'task_name': openapi.Schema(type=openapi.TYPE_STRING),
                                'image_path': openapi.Schema(type=openapi.TYPE_STRING),
                                'endpoint': openapi.Schema(type=openapi.TYPE_STRING),
                                'run_count': openapi.Schema(type=openapi.TYPE_INTEGER, description="Number of times this task has been run"),
                                'created_at': openapi.Schema(type=openapi.TYPE_STRING, format='date-time'),
                                'updated_at': openapi.Schema(type=openapi.TYPE_STRING, format='date-time'),
                            }
                        )
                    )
                }
            )
        ),
        401: openapi.Response(
            description="Unauthorized",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'detail': openapi.Schema(
                        type=openapi.TYPE_STRING,
                        example="Authentication credentials were not provided."
                    )
                }
            )
        )
    }
)