from rest_framework import serializers
from core.models import *

# class OriginalImages(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     file_name = serializers.CharField(max_length=250) # could switch to FilePathField TODO: try that
#     meta_data = serializers.TextField()



# class ModdedImages(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     file_name = serializers.CharField(max_length=250) # could switch to FilePathField TODO: try that


class KeySerializer(serializers.ModelSerializer):
    class Meta:
        model = Key
        fields = ['id', 'value']

    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing Key instance.
    #     """
    #     instance.value = validated_data.get('value', instance.value)
    #     instance.save()
    #     return instance
