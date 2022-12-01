from django.shortcuts import render  # TODO: Remove if not used
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from core.models import *
from core.serializers import *

from django.http import HttpResponse
import datetime

def index(request):
    try:
        return HttpResponse("index loaded sucessfully", status=200)
    except Exception as error:
        return HttpResponse(f"creation failed. Error: {error}")


@csrf_exempt
def key_list(request):
    """
    List all keys
    """
    if request.method == 'GET':
        try:
            serializer = KeySerializer(Key.objects.all(), many=True)
            return JsonResponse(serializer.data, safe=False)
        except Exception as error:
            return HttpResponse(f"Error: {error}", status=400)

    else:
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def key_create(request):
    """
    Create a new key with default value 0
    """
    if request.method == 'GET':
        data = JSONParser().parse(request)
        serializer = KeySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = KeySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def key_detail(request, pk):
    """
    Retrieve, update or delete keys.
    """
    try:
        key = Key.objects.get(pk=pk)
    except Key.DoesNotExist:
        return HttpResponse(status=404)

    # if request.method == 'GET':
    #     data = key.value
    #     serializer = KeySerializer(key, data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data)
    #     return JsonResponse(serializer.errors, status=400)


