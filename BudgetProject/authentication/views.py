from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.response import Response


# Create your views here.

class RegisterView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
