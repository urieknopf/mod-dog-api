from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [
    path('', index),  # TODO: Fix index?
    path('admin/', admin.site.urls),
    path('keys/', key_list),
    path('key/<int:pk>/', key_detail),
    path('key/create/', key_create),
]
