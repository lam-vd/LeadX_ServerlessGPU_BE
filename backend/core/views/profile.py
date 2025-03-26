from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from core.serializers.change_profile import UpdateProfileSerializer
from core.swagger.profile import update_profile_swagger_schema
from core.utils.response_formatter import success_response, error_response

class UpdateProfileView(APIView):
    permission_classes = [IsAuthenticated]

    @update_profile_swagger_schema
    def put(self, request):
        user = request.user
        serializer = UpdateProfileSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return success_response(
                data=serializer.data,
                message="profile_updated",
                status_code=status.HTTP_200_OK
            )
        return error_response(
            errors=serializer.errors,
            message="validation_error",
            status_code=status.HTTP_400_BAD_REQUEST
        )