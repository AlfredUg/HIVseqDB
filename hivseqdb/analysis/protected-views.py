from analysis.models import AnalysisResults, NewAnalysis  
from analysis.tasks import run_quasiflow
from django.http import HttpResponseRedirect
from django.views import generic
from analysis.forms import NewAnalysisForm
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from analysis.helpers import charts
# Create your views here.

class CreateNewAnalysisView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    template_name = 'analysis/new-analysis.html'
    form_class = NewAnalysisForm

    def post(self, *args, **kwargs):
          form = NewAnalysisForm(data=self.request.POST)      
          if form.is_valid():
              project_ID=self.request.POST['project_ID']
              description=self.request.POST['description']
              email=self.request.POST['email']
              consensus_Percentage=self.request.POST['consensus_Percentage']
              error_Rate=self.request.POST['error_Rate']
              length_Cutoff=self.request.POST['length_Cutoff']
              minimum_Allele_Count=self.request.POST['minimum_Allele_Count']
              minimum_Mutation_Frequency=self.request.POST['minimum_Mutation_Frequency']
              minimum_Read_Depth=self.request.POST['minimum_Read_Depth']
              minimum_Variant_Quality=self.request.POST['minimum_Variant_Quality']
              mutation_Database=self.request.POST['mutation_Database']
              score_Cutoff=self.request.POST['score_Cutoff']
              target_Coverage=self.request.POST['target_Coverage']

              analysis_instance=NewAnalysis(
                project_ID=project_ID,
                description=description,
                email=email,
                consensus_Percentage=consensus_Percentage,
                error_Rate=error_Rate,
                length_Cutoff=length_Cutoff,
                minimum_Allele_Count=minimum_Allele_Count,
                minimum_Mutation_Frequency=minimum_Mutation_Frequency,
                minimum_Read_Depth=minimum_Read_Depth,
                minimum_Variant_Quality=minimum_Variant_Quality,
                mutation_Database=mutation_Database,
                score_Cutoff=score_Cutoff,
                target_Coverage=target_Coverage
              )
              analysis_instance.save() #save analysis parameters in database
              run_quasiflow.delay(project_ID) # run analysis in background
              messages.success(self.request, 'We are on it! Your analysis is running in the background.')
              return HttpResponseRedirect(self.request.path_info)

class AnalysisResultsView(LoginRequiredMixin, generic.ListView):
    model = AnalysisResults
    queryset = AnalysisResults.objects.all().order_by('analysis_results_id')
    template_name = 'analysis/analysis-results.html'
    paginate_by = 10

class ProjectAnalysisResultsDetailView(LoginRequiredMixin, generic.ListView):
    model = AnalysisResults
    template_name = 'analysis/detailed-project-analysis-results.html'
    paginate_by = 10

    def get_queryset(self):
        return AnalysisResults.objects.filter(project_ID=self.kwargs['project_ID'])

class SampleAnalysisResultsDetailView(LoginRequiredMixin, generic.ListView):
    model = AnalysisResults
    template_name = 'analysis/detailed-sample-analysis-results.html'
    paginate_by = 10

    def get_queryset(self):
        return AnalysisResults.objects.filter(sample_ID=self.kwargs['sample_ID'])

class ProjectMinorityVariantsView(LoginRequiredMixin, generic.ListView):
    template_name = 'analysis/minority-variants.html'

    def get_queryset(self):
        test_chart = charts()
        return test_chart
