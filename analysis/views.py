from analysis.models import AnalysisResults, NewAnalysis ,MinorityVariantsResult 
from analysis.tasks import run_quasiflow
from django.http import HttpResponseRedirect
from django.views import generic
from analysis.forms import NewAnalysisForm
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from analysis.helpers import project_gene_drms
from django.shortcuts import render
#from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


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
    context_object_name = 'results'   
    #paginate_by = 30

class ProjectAnalysisResultsDetailView(generic.ListView):
    model = AnalysisResults
    template_name = 'analysis/detailed-project-analysis-results.html'
    #paginate_by = 5
    context_object_name = 'results'   

    def get_queryset(self):
        return AnalysisResults.objects.filter(project_ID=self.kwargs['project_ID'])

class SampleAnalysisResultsDetailView(LoginRequiredMixin, generic.ListView):
    model = AnalysisResults
    template_name = 'analysis/detailed-sample-analysis-results.html'
    paginate_by = 5

    def get_queryset(self):
        return AnalysisResults.objects.filter(sample_ID=self.kwargs['sample_ID'])

class ProjectMinorityVariantsView(generic.ListView):
    model = MinorityVariantsResult
    template_name = 'analysis/minority-variants.html'
    #paginate_by = 5
    context_object_name = 'results'   

    def get_queryset(self):
        return MinorityVariantsResult.objects.filter(project=self.kwargs['project'])

    def get_context_data(self, **kwargs):

        context=super().get_context_data(**kwargs)
        context['mdrms']='' #Major DRMS
        context['adrms']='' #accessory DRMS

        return context

@login_required
def minority(request, project):

    project_variants = MinorityVariantsResult.objects.filter(project=project)
    #paginator = Paginator(project_variants, 5)
    #page = request.GET.get('page', 1)
    #project_variants = paginator.page(page)
    pr_drms = project_gene_drms(project, 'PR')
    print(pr_drms)
    
    rt_drms = project_gene_drms(project, 'RT')
    print(rt_drms)
    
    #int_drms = project_gene_drms(project, 'IN')
    #print(int_drms)

    context={
        'pr_variants': pr_drms[0],
        'pr_majority': pr_drms[1],
        'pr_minority': pr_drms[2],
        'rt_variants': rt_drms[0],
        'rt_majority': rt_drms[1],
        'rt_minority': rt_drms[2],
        'project_variants': project_variants

        #'int_variants': int_drms[0],
        #'int_majority': int_drms[1],
        #'int_minority': int_drms[2],
    }
    print(context)
    return render(request, 'analysis/minority-variants.html', context=context)
