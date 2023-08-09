from django.contrib import admin
from django.urls import path
from analysis.views import * #minority, CreateNewAnalysisView, AnalysisResultsView, ProjectAnalysisResultsDetailView, SampleAnalysisResultsDetailView, ProjectMinorityVariantsView

urlpatterns = [
    path('analysis/create/', CreateNewAnalysisView.as_view(), name='newAnalysisForm'),
    path('analysis/results/', AnalysisResultsView.as_view(), name='analysisResults'),
    path('analysis/minority-variants/project/<slug:project>', minority, name='projectMinorityVariants'),
    path('analysis/minority-variants/sample/<slug:sample>', minority_sample, name='sampleMinorityVariants'),
    path('analysis/drug-resistance-report/<slug:sample>', drug_resistance_report, name='sampleDrugResistance'),
]
