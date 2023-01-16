from django.contrib import admin
from django.urls import path
from search.views import SampleView, NGSdataView, AdvancedSearchView

urlpatterns = [
    path('hivseqdb/search/ngs-data/', NGSdataView.as_view(), name='searchngs'),
    path('hivseqdb/search/sample-data/', SampleView.as_view(), name='searchsample'),
    path('hivseqdb/search/advanced/', AdvancedSearchView.as_view(), name='advancedsearch'),
]
