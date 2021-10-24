from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Rainfall
from .serializers import RainfallSerializer

# Create your views here.

@api_view(['GET'])
def dataList(request):
    rainfall = Rainfall.objects.all()
    serializer = RainfallSerializer(rainfall, many=True)

    return Response(serializer.data)