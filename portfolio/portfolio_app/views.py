from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Message
from .serializers import MessageSerializer
from rest_framework import generics , permissions ,exceptions
import logging
from django.shortcuts import render

logger = logging.getLogger(__name__)

def index(request):
    return render(request, 'portfolio_app/index.html')

class MessageData(generics.GenericAPIView):
    def post(self, request):
        try:
            serializer = MessageSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            msg = serializer.validated_data
            dep = Message.objects.create(**msg)
            dep_serializer = MessageSerializer(dep)
            return Response({'status': 'success', 'message': 'Successfully Added', 'data': dep_serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.exception('Exception {}'.format(e.args))
            return Response({'status': 'fail', 'message': 'Something went wrong. Please try again'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request):
        try:
            dept = Message.objects.all()
            dept_serializer = MessageSerializer(dept, many=True)
            return Response({'status': 'success', 'message': 'Displayed', 'data': dept_serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.exception('Exception {}'.format(e.args))
            return Response({'status': 'fail', 'message': 'Something went wrong. Please try again'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
