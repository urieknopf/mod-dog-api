from rest_framework import serializers

from core.models import *

class KeySerializer(serializers.ModelSerializer):
    class Meta:
        model = Key
        fields = ['id', 'value']

class OriginalImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = OriginalImage
        fields = ['id', 'created', 'file', 'breed_name', 'file_name', 'original_url']
