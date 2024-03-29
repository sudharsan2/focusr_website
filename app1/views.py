from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . serializers import enquery_serializer,apply_serializer


# Create your views here.

class save_api_enquery(APIView):
    def post(self,request):
        data = request.data
        serializer = enquery_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
        return Response("successfully saved")
    
class save_api_apply(APIView):
    def post(self,request):
        data = request.data
        serializer = apply_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
        return Response("successfully saved")
    