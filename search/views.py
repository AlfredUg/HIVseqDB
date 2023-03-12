from django.shortcuts import render
from django.views import generic
from uploads.models import Sample, Project
from search.forms import AdvancedSearchForm
# Create your views here.

class SampleView(generic.ListView):
    model = Sample
    queryset = Sample.objects.all().order_by('sample')
    template_name = 'search/sample-data.html'
    #paginate_by = 10
    context_object_name = 'results'   

class NGSdataView(generic.ListView):
    model = Project
    queryset = Project.objects.all().order_by('project_ID')
    template_name = 'search/ngs-data.html'
    #paginate_by = 10
    context_object_name = 'results'   


class AdvancedSearchView(generic.ListView):
    template_name = 'search/sample-data-advanced.html'
    queryset = Sample.objects.all().order_by('sample')

    