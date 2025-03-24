from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.serializers.change_profile import UpdateProfileSerializer
from core.messages import SUCCESS_MESSAGES, ERROR_MESSAGES
from core.swagger.profile import update_profile_swagger_schema

class UpdateProfileView(APIView):
    permission_classes = [IsAuthenticated]

    @update_profile_swagger_schema
    def put(self, request):
        user = request.user
        serializer = UpdateProfileSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'data': serializer.data,
                'status': status.HTTP_200_OK,
                'message': SUCCESS_MESSAGES['profile_updated']
            }, status=status.HTTP_200_OK)
        return Response({
            'data': {},
            'status': status.HTTP_400_BAD_REQUEST,
            'message': ERROR_MESSAGES['validation_error'],
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)