from django.contrib import admin
from django.urls import path
from analysis.views import CreateNewAnalysisView, AnalysisResultsView, ProjectAnalysisResultsDetailView, SampleAnalysisResultsDetailView

urlpatterns = [
    path('analysis/create/', CreateNewAnalysisView.as_view(), name='newAnalysisForm'),
    path('analysis/results/', AnalysisResultsView.as_view(), name='analysisResults'),
    path('analysis/detailed-project-results/<slug:project_ID>', ProjectAnalysisResultsDetailView.as_view(), name='projectAnalysisResultsDetails'),
    path('analysis/detailed-sample-results/<slug:sample_ID>', SampleAnalysisResultsDetailView.as_view(), name='sampleAnalysisResultsDetails'),
]
