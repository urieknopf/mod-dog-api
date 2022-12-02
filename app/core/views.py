from django.shortcuts import render  # TODO: Remove if not used
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
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
@api_view(['GET', 'POST'])
def key_list(request):
    """
    List all keys, or create a new key with default value of 0
    """
    if request.method == 'GET':
        try:
            serializer = KeySerializer(Key.objects.all(), many=True)
            return JsonResponse(serializer.data, safe=False)
        except Exception as error:
            return HttpResponse(f"Error: {error}", status=400)
    elif request.method == 'POST':
        try:
            key = Key()
            key.save()
            serializer = KeySerializer(key)
            return JsonResponse(serializer.data, status=201)
        except Exception as error:
            return HttpResponse(f"Error: {error}", status=400)
    else:
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
@api_view(['GET', 'PUT'])
def key_detail(request, pk):
    """
    Retrieve, update or delete keys.
    """
    try:
        key = Key.objects.get(pk=pk)
    except Key.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = KeySerializer(key)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':  # TODO: Get this to work
        key.value = key.value + 1
        key.save()
        serializer = KeySerializer(key)
        return JsonResponse(serializer.data)
        



