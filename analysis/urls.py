from django.contrib import admin
from django.urls import path
from analysis.views import CreateNewAnalysisForm, AnalysisResultsView, DetailedAnalysisView

urlpatterns = [
    path('hivseqdb/analysis/create/', CreateNewAnalysisForm.as_view(), name='newAnalysisForm'),
    path('hivseqdb/analysis/results/', AnalysisResultsView.as_view(), name='analysisResults'),
    path('hivseqdb/analysis/detailed-results/', DetailedAnalysisView.as_view(), name='analysisResultsDetails'),
]
