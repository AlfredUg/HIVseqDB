from django.shortcuts import render
from django.views import generic
from search.models import Sample
from search.forms import AdvancedSearchForm
from uploads.models import Project
# Create your views here.

class SampleView(generic.ListView):
    model = Sample
    queryset = Sample.objects.all().order_by('sample_id')
    template_name = 'search/sample-data.html'
    paginate_by = 2

class NGSdataView(generic.ListView):
    model = Project
    queryset = Project.objects.all().order_by('project_ID')
    template_name = 'search/ngs-data.html'
    paginate_by = 2

class AdvancedSearchView(generic.ListView):
    template_name = 'search/sample-data-advanced.html'
    queryset = Sample.objects.all().order_by('sample_id')

    