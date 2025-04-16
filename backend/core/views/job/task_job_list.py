from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
from core.models.job import Job
from core.serializers.task_job_list import TaskJobListSerializer
from core.utils.response_formatter import success_response
from core.swagger.task_job_list_swagger import swagger_task_job_list
from django.conf import settings

class TaskJobListView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_task_job_list
    def get(self, request):
        filters = self.build_filters(request)
        queryset = self.get_filtered_queryset(filters)
        paginated_queryset, pagination_data = self.paginate_queryset(queryset, request)
        serializer = TaskJobListSerializer(paginated_queryset, many=True)
        return success_response(
            data={"results": serializer.data, **pagination_data},
            message="task_job_list_retrieved_successfully",
            status_code=200
        )

    def build_filters(self, request):
        """Build filters based on query parameters."""
        filters = Q(task__user=request.user, deleted_at__isnull=True)
        if status := request.query_params.get("status"):
            status_mapping = {
                "pending": Job.Status.PENDING,
                "running": Job.Status.RUNNING,
                "completed": Job.Status.COMPLETED,
                "failed": Job.Status.FAILED,
                "stopped": Job.Status.STOPPED,
            }
            status_value = status_mapping.get(status)
            if status_value is not None:
                filters &= Q(status=status_value)
        if gpu_type := request.query_params.get("gpu_type"):
            filters &= Q(gpu_type__name__icontains=gpu_type)
        if task_name := request.query_params.get("task_name"):
            filters &= Q(task__task_name__icontains=task_name)
        if start_date := request.query_params.get("start_date"):
            filters &= Q(created_at__date__gte=start_date)
        if end_date := request.query_params.get("end_date"):
            filters &= Q(created_at__date__lte=end_date)
        return filters

    def get_filtered_queryset(self, filters):
        return Job.objects.filter(filters).select_related("task", "gpu_type").order_by("-created_at")

    def paginate_queryset(self, queryset, request):
        """Paginate the queryset."""
        paginator = PageNumberPagination()
        try:
            page_size = int(request.query_params.get("page_size", settings.DEFAULT_PAGE_SIZE))
            page_size = min(page_size, settings.MAX_PAGE_SIZE)
        except ValueError:
            page_size = settings.DEFAULT_PAGE_SIZE
        paginator.page_size = page_size
        paginated_queryset = paginator.paginate_queryset(queryset, request)
        pagination_data = {
            "count": paginator.page.paginator.count,
            "next": paginator.get_next_link(),
            "previous": paginator.get_previous_link(),
        }
        return paginated_queryset, pagination_data