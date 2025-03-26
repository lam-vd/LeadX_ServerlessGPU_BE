from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from core.serializers.change_password import ChangePasswordSerializer
from core.swagger.change_password import change_password_swagger_schema
from core.utils.response_formatter import success_response, error_response

class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    @change_password_swagger_schema
    def post(self, request):
        user = request.user
        serializer = ChangePasswordSerializer(data=request.data, context={'user': user})
        if serializer.is_valid():
            user.set_password(serializer.validated_data['new_password'])
            user.save()
            return success_response(
                data={},
                message="password_changed",
                status_code=status.HTTP_200_OK
            )
        return error_response(
            errors=serializer.errors,
            message="validation_error",
            status_code=status.HTTP_400_BAD_REQUEST
        )