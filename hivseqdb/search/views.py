from django.shortcuts import render
from django.views import generic
from uploads.models import Sample, Project
from search.forms import AdvancedSearchForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages #import messages
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class SampleView(LoginRequiredMixin, generic.ListView):
    model = Sample
    queryset = Sample.objects.all().order_by('sample')
    template_name = 'search/sample-data.html'
    #paginate_by = 10
    context_object_name = 'results'   

class NGSdataView(LoginRequiredMixin, generic.ListView):
    model = Project
    queryset = Project.objects.all().order_by('projectID')
    template_name = 'search/ngs-data.html'
    #paginate_by = 10
    context_object_name = 'results'


class AdvancedSearchView(generic.ListView):
    template_name = 'search/sample-data-advanced.html'
    queryset = Sample.objects.all().order_by('sample')

    