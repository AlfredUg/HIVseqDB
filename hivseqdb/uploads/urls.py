from django.contrib import admin
from django.urls import path
from uploads.views import CreateDataUpload, CreateDataUploadSingle, CreateDataUploadConsensusSingle, CreateDataUploadConsensusBatch

urlpatterns = [
    path('uploads/ngs-data-batch/', CreateDataUpload.as_view(), name='data_uploads'),
    path('uploads/ngs-data-single/', CreateDataUploadSingle.as_view(), name='data_uploads_single'),
    path('uploads/consensus-data-single/', CreateDataUploadConsensusSingle.as_view(), name='data_uploads_consensus_single'),
    path('uploads/consensus-data-batch/', CreateDataUploadConsensusBatch.as_view(), name='data_uploads_consensus_batch'),
]
