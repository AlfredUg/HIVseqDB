from django.contrib import admin
from django.urls import path
from uploads.views import CreateFastqUploadForm,CreateSampleUploadForm

urlpatterns = [
    path('uploads/ngs-data/', CreateFastqUploadForm.as_view(), name='ngs_uploads'),
    path('uploads/sample-data/', CreateSampleUploadForm.as_view(), name='sample_uploads'),
]
