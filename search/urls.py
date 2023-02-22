from django.contrib import admin
from django.urls import path
from search.views import SampleView, NGSdataView, AdvancedSearchView

urlpatterns = [
    path('browse/ngs-data/', NGSdataView.as_view(), name='searchngs'),
    path('browse/sample-data/', SampleView.as_view(), name='searchsample'),
    path('search/advanced/', AdvancedSearchView.as_view(), name='advancedsearch'),
]
