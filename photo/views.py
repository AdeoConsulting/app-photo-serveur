from django.shortcuts import get_object_or_404

from .serializer import PhotoSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class PhotoList(APIView):
	def post(request, format=None):
		serializer = PhotoSerializer(data=request.data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)