from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from core.models.gpu_type import GpuType
from core.serializers.gpu_type import GpuTypeSerializer
from core.utils.response_formatter import success_response
from core.swagger.gpu_type_list_swagger import gpu_type_list_swagger

class GpuTypeListView(APIView):
    permission_classes = [IsAuthenticated]

    @gpu_type_list_swagger
    def get(self, request):
        gpu_types = GpuType.objects.filter(deleted_at__isnull=True).order_by("name")
        serializer = GpuTypeSerializer(gpu_types, many=True)
        return success_response(
            data=serializer.data,
            message="gpu_type_list_retrieved_successfully",
            status_code=200
        )