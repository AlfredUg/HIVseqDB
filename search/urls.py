from django.contrib import admin
from django.urls import path
from search.views import SampleView, NGSdataView, AdvancedSearchView

urlpatterns = [
    path('search/ngs-data/', NGSdataView.as_view(), name='searchngs'),
    path('search/sample-data/', SampleView.as_view(), name='searchsample'),
    path('search/advanced/', AdvancedSearchView.as_view(), name='advancedsearch'),
]
