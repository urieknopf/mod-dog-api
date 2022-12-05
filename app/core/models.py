from django.db import models

class OriginalImage(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    file = models.ImageField(upload_to='images/dogs/', height_field=None, width_field=None, max_length=100, null=False)
    breed_name = models.CharField(max_length=250, default='') 
    file_name = models.CharField(max_length=250, default='') 
    original_url = models.CharField(max_length=250, default='') 

    class Meta:
        ordering = ['created']


# class ModdedImages(models.Model):
#     created = models.DateTimeField(auto_now_add=True)
#     file_name = models.CharField(max_length=250) # could switch to FilePathField TODO: try that

#     class Meta:
#         ordering = ['created']


class Key(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    value = models.IntegerField(default='0')

    class Meta:
        ordering = ['created']