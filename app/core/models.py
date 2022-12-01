from django.db import models


class OriginalImages(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    file_name = models.CharField(max_length=250) # could switch to FilePathField TODO: try that
    meta_data = models.TextField()

    class Meta:
        ordering = ['created']


class ModdedImages(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    file_name = models.CharField(max_length=250) # could switch to FilePathField TODO: try that

    class Meta:
        ordering = ['created']


class Key(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    value = models.IntegerField(default='0')

    class Meta:
        ordering = ['created']