from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from core.models.task import Task
from core.serializers.task import TaskSerializer
from django.db.models import Count, Q
from core.swagger.task_list_swagger import task_list_swagger
import logging

logger = logging.getLogger(__name__)

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