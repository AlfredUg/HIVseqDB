from django.contrib import admin
from django.urls import path
from uploads.views import CreateDataUpload

urlpatterns = [
    path('uploads/ngs-data/', CreateDataUpload.as_view(), name='data_uploads'),
]
