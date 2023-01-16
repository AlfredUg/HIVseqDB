from django.shortcuts import render
from analysis.models import AnalysisResults  
from django import forms
from django.views import generic
from analysis.forms import NewAnalysisForm
# Create your views here.

class CreateNewAnalysisForm(generic.CreateView):
    template_name = 'analysis/new-analysis.html'
    form_class = NewAnalysisForm

class AnalysisResultsView(generic.ListView):
    model = AnalysisResults
    queryset = AnalysisResults.objects.all().order_by('analysis_results_id')
    template_name = 'analysis/analysis-results.html'
    paginate_by = 2

class DetailedAnalysisView(generic.ListView):
    context_object_name = 'analysisResultsDetails'
    model = AnalysisResults
    template_name = 'analysis/detailed-analysis-results.html'

 