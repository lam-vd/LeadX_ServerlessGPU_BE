from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

task_list_swagger = swagger_auto_schema(
    operation_summary="Get task list",
    operation_description="Retrieve a paginated list of tasks for the current user, including run count and other details.",
    responses={
        200: openapi.Response(
            description="Success",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'data': openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'count': openapi.Schema(
                                type=openapi.TYPE_INTEGER,
                                description="Total number of tasks"
                            ),
                            'next': openapi.Schema(
                                type=openapi.TYPE_STRING,
                                format=openapi.FORMAT_URI,
                                description="URL to the next page of results, or null if there is no next page"
                            ),
                            'previous': openapi.Schema(
                                type=openapi.TYPE_STRING,
                                format=openapi.FORMAT_URI,
                                description="URL to the previous page of results, or null if there is no previous page"
                            ),
                            'results': openapi.Schema(
                                type=openapi.TYPE_ARRAY,
                                items=openapi.Schema(
                                    type=openapi.TYPE_OBJECT,
                                    properties={
                                        'task_name': openapi.Schema(
                                            type=openapi.TYPE_STRING,
                                            description="Name of the task"
                                        ),
                                        'description': openapi.Schema(
                                            type=openapi.TYPE_STRING,
                                            description="Description of the task"
                                        ),
                                        'source_code': openapi.Schema(
                                            type=openapi.TYPE_STRING,
                                            description="Source code of the task (write-only)"
                                        ),
                                        'endpoint': openapi.Schema(
                                            type=openapi.TYPE_STRING,
                                            description="Endpoint for the task"
                                        ),
                                        'run_count': openapi.Schema(
                                            type=openapi.TYPE_INTEGER,
                                            description="Number of times this task has been run"
                                        ),
                                        'created_at': openapi.Schema(
                                            type=openapi.TYPE_STRING,
                                            format='date-time',
                                            description="Timestamp when the task was created"
                                        ),
                                        'updated_at': openapi.Schema(
                                            type=openapi.TYPE_STRING,
                                            format='date-time',
                                            description="Timestamp when the task was last updated"
                                        ),
                                    }
                                )
                            )
                        }
                    ),
                    'status': openapi.Schema(
                        type=openapi.TYPE_INTEGER,
                        description="HTTP status code"
                    ),
                    'message': openapi.Schema(
                        type=openapi.TYPE_STRING,
                        description="Response message"
                    ),
                    'errors': openapi.Schema(
                        type=openapi.TYPE_STRING,
                        description="Error details (if any)"
                    )
                }
            )
        ),
        404: openapi.Response(
            description="Invalid page number",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'data': openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        description="Empty object",
                        default={}
                    ),
                    'status': openapi.Schema(
                        type=openapi.TYPE_INTEGER,
                        description="HTTP status code",
                        example=404
                    ),
                    'message': openapi.Schema(
                        type=openapi.TYPE_STRING,
                        description="Error message",
                        example="Invalid page number"
                    ),
                    'errors': openapi.Schema(
                        type=openapi.TYPE_STRING,
                        description="Details about the error",
                        example="Invalid page."
                    )
                }
            )
        ),
        500: openapi.Response(
            description="Unexpected error",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'data': openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        description="Empty object",
                        default={}
                    ),
                    'status': openapi.Schema(
                        type=openapi.TYPE_INTEGER,
                        description="HTTP status code",
                        example=500
                    ),
                    'message': openapi.Schema(
                        type=openapi.TYPE_STRING,
                        description="Error message",
                        example="An unexpected error occurred"
                    ),
                    'errors': openapi.Schema(
                        type=openapi.TYPE_STRING,
                        description="Details about the error",
                        example="Error details here"
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