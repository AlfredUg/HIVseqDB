from django.contrib import admin
from django.urls import path
from analysis.views import CreateNewAnalysisForm, AnalysisResultsView, DetailedAnalysisView

urlpatterns = [
    path('analysis/create/', CreateNewAnalysisForm.as_view(), name='newAnalysisForm'),
    path('analysis/results/', AnalysisResultsView.as_view(), name='analysisResults'),
    path('analysis/detailed-results/', DetailedAnalysisView.as_view(), name='analysisResultsDetails'),
]
