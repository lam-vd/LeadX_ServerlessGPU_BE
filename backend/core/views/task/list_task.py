from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from core.models.task import Task
from core.serializers.task import TaskSerializer
from django.db.models import Count, Q
from core.swagger.task_list_swagger import task_list_swagger
from core.utils.response_formatter import success_response, error_response

class TaskListView(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    @task_list_swagger
    def get_queryset(self):
        return Task.objects.filter(
            user=self.request.user,
            deleted_at__isnull=True
        ).annotate(
            run_count=Count('job', filter=Q(job__deleted_at__isnull=True))
        ).order_by('-created_at')

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            page = self.paginate_queryset(queryset)
            if not queryset.exists():
                return self.format_empty_response()
            return self.format_paginated_response(page) if page else self.format_full_response(queryset)
        except NotFound as e:
            return error_response(errors=str(e), message="invalid_page_number", status_code=404)
        except Exception as e:
            return error_response(errors=str(e), message="an_unexpected_error_occurred", status_code=500)

    def format_empty_response(self):
        empty_data = {
            "count": 0,
            "next": None,
            "previous": None,
            "results": []
        }
        return success_response(data=empty_data, message="task_list_retrieved_successfully", status_code=200)

    def format_paginated_response(self, page):
        serializer = self.get_serializer(page, many=True)
        paginated_data = self.get_paginated_response(serializer.data).data
        return success_response(paginated_data, "task_list_retrieved_successfully", 200)

    def format_full_response(self, queryset):
        serializer = self.get_serializer(queryset, many=True)
        return success_response(serializer.data, "task_list_retrieved_successfully", 200)