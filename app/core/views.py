import json
import requests
import urllib

from django.core.files import File
from django.core.files.base import ContentFile
from django.core.files.temp import NamedTemporaryFile
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render  # TODO: Remove if not used
from django.views.decorators.csrf import csrf_exempt\

from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser  # TODO: Remove if not used

from core.models import *
from core.serializers import *


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


@csrf_exempt
@api_view(['GET', 'PUT'])
def key_detail(request, pk):
    """
    Retrieve or update key
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
        

@csrf_exempt
@api_view(['GET', 'POST'])
def get_dogs(request):
    """
    Service to get dogs from dog api and add to model
    """
    if request.method == 'GET':
        try:
            serializer = OriginalImageSerializer(OriginalImage.objects.all(), many=True)
            return JsonResponse(serializer.data, safe=False)
        except Exception as error:
            return HttpResponse(f"Error: {error}", status=400)
    elif request.method == 'POST':

        # Currently not working, puts null in place of images... 
        # despite the fact that null isn't supposed to be accepted by imageField...
        try:
            amount = 24
            api_url = f'https://dog.ceo/api/breeds/image/random/{amount}'
            dog_url_list = json.loads(requests.get(api_url).text)['message']
            count = 0

            for url in dog_url_list:
                response = requests.get(url)
                if response.status_code == 200:
                    count += 1
                    image = OriginalImage()
                    image.original_url = url
                    image.breed_name = url.split('/')[4]
                    image.file_name = url.split('/')[5]
                    image.file = ContentFile(response.content)
                    image.save()

            return HttpResponse(f'{count} images loaded to database succesfully.', status='200')
        except Exception as error:
            return HttpResponse(f'error: {error}', status=404)
        
# TODO: Add error catch that goes and retrieves additional images if any fail so that it always adds 24, SET A LIMIT TO NUM OF RETRIES


