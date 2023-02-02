from django.contrib import admin
from django.urls import path
from uploads.views import CreateFastqUpload,CreateSampleUpload

urlpatterns = [
    path('uploads/ngs-data/', CreateFastqUpload.as_view(), name='ngs_uploads'),
    path('uploads/sample-data/', CreateSampleUpload.as_view(), name='sample_uploads'),
]
