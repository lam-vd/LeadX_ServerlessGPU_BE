# backend/core/views/activation.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.serializers.activation import ActivationSerializer
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from core.messages import SUCCESS_MESSAGES
from core.swagger.activation import activation_swagger_schema

@method_decorator(csrf_protect, name='dispatch')
class ActivationView(APIView):
    @activation_swagger_schema
    def post(self, request):
        serializer = ActivationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': SUCCESS_MESSAGES['account_activated']}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)