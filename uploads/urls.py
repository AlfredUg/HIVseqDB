from django.contrib import admin
from django.urls import path
from uploads.views import CreateFastqUploadForm,CreateSampleUploadForm

urlpatterns = [
    path('hivseqdb/uploads/ngs-data', CreateFastqUploadForm.as_view(), name='ngs_uploads'),
    path('hivseqdb/uploads/sample-data', CreateSampleUploadForm.as_view(), name='sample_uploads'),
]
