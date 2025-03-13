from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.serializers.activation import ActivationSerializer
from drf_yasg.utils import swagger_auto_schema
from core.messages import SUCCESS_MESSAGES
from core.swagger.activation import activation_swagger_schema

class ActivationView(APIView):
    @swagger_auto_schema(**activation_swagger_schema)
    def get(self, request):
        token = request.query_params.get('token')
        serializer = ActivationSerializer(data={'token': token})
        if serializer.is_valid():
            serializer.save()
            return Response({'message': SUCCESS_MESSAGES['account_activated']}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)