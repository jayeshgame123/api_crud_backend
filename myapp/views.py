from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import JsonResponse
from django.http.response import Http404
from .models import User
from .serializers import UserSerializer
# Create your views here.

class UserView(APIView):

    def get(self,request,pk=None):
        if pk:
            data = User.objects.get(pk=pk)
            serializer = UserSerializer(data)
        else:
            data = User.objects.all()
            serializer = UserSerializer(data, many=True)
        return Response(serializer.data)

    def post(self,request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response("Add Successfully")
        return Response("Failed to add")