from analysis.models import AnalysisResults, NewAnalysis ,MinorityVariantsResult 
from analysis.tasks import run_quasiflow
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from analysis.forms import NewAnalysisForm
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from analysis.helpers import project_gene_drms, json_normalise_helper, sample_gene_drms
from django.shortcuts import render
#from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

import os
from django.conf import settings
import json, requests
import pandas as pd

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
              #messages.success(self.request, 'Once the run is done, you can access results at:')
              return HttpResponseRedirect(self.request.path_info)

class AnalysisResultsView(LoginRequiredMixin, generic.ListView):
    model = AnalysisResults
    queryset = AnalysisResults.objects.all().order_by('analysis_results_id')
    template_name = 'analysis/analysis-results.html'
    context_object_name = 'results'   
    #paginate_by = 30

class ProjectAnalysisResultsDetailView(LoginRequiredMixin, generic.ListView):
    model = AnalysisResults
    template_name = 'analysis/analysis-results.html'
    #paginate_by = 5
    context_object_name = 'results'   

    def get_queryset(self):
        return AnalysisResults.objects.filter(project_ID=self.kwargs['project'])

class SampleAnalysisResultsDetailView(LoginRequiredMixin, generic.ListView):
    model = AnalysisResults
    template_name = 'analysis/analysis-results.html'
    context_object_name = 'results'   
    #paginate_by = 5

    def get_queryset(self):
        return AnalysisResults.objects.filter(sample_ID=self.kwargs['sample'])

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

@login_required
def minority_sample(request, sample):
    sample_variants = MinorityVariantsResult.objects.filter(sample=sample)
    #paginator = Paginator(project_variants, 5)
    #page = request.GET.get('page', 1)
    #project_variants = paginator.page(page)
    pr_drms = sample_gene_drms(sample, 'PR')
    print(pr_drms)

    #this out put has five lists
    #1. variants
    #2. major
    #3. major_freq
    #4. major_cov
    #5. minor
    #6. minor_freq
    #7. minor_cov

    rt_drms = sample_gene_drms(sample, 'RT')
    print(rt_drms)
    
    #int_drms = project_gene_drms(project, 'IN')
    #print(int_drms)

    context={
        'pr_variants': pr_drms[0],
        'pr_majority': pr_drms[1],
        'pr_majority_freq': pr_drms[2],
        'pr_majority_cov': pr_drms[3],
        'pr_minority': pr_drms[4],
        'pr_minority_freq': pr_drms[5],
        'pr_minority_cov': pr_drms[6],

        'rt_variants': rt_drms[0],
        'rt_nrti': rt_drms[1],
        'rt_nrti_freq': rt_drms[2],
        'rt_nrti_cov': rt_drms[3],
        'rt_nnrti': rt_drms[4],
        'rt_nnrti_freq': rt_drms[5],
        'rt_nnrti_cov': rt_drms[6],
        
        'sample_variants': sample_variants

        #'int_variants': int_drms[0],
        #'int_majority': int_drms[1],
        #'int_minority': int_drms[2],
    }
    print(context)
    return render(request, 'analysis/minority-variants-sample.html', context=context)

@login_required
def drug_resistance_report(request, sample):
    # pdf_resp = HttpResponse(content_type='application/pdf')
    
    url="https://raw.githubusercontent.com/AlfredUg/ngs_hivdb/master/data/"+sample+".json"
    json_response = requests.get(url)
    data = json.loads(json_response.text)
    # Using the sample ID, look through analysis results and get a corresponding project ID
    # project = ''.join(AnalysisResults.objects.filter(sample_ID=sample).values('project_ID')[1].values())
    # look up corresponding JSON file in the analyses directory
    # json_report_path=os.path.join(settings.MEDIA_ROOT,'ngs/analyses/', project, sample+'.json')
    # read the json and generate report
    # json_report = open(json_report_path)
    # data = json.load(json_report)
    seqName=data[0]['inputSequence']['header']
    print(seqName)

    subType=data[0]['subtypeText']
    print(subType)

    genes_data=data[0]['alignedGeneSequences']
    genes_ranges=pd.json_normalize(genes_data, meta=['firstAA', 'lastAA', ['gene','name']])[['firstAA','lastAA','gene.name']]
    genes_ranges.columns=['firstAA','lastAA','gene']

    drug_resistance=data[0]['drugResistance']
    drug_resistance=pd.json_normalize(drug_resistance, record_path=['drugScores',], 
                         meta=[['version', 'text'], 
                           ['version','publishDate'], 
                           ['gene', 'name']
                          ])
    drug_resistance.columns = ['Score', 'partialScores', 'Susceptibility', 'DrugClass', 'DrugName',
       'DrugDisplayAbbr', 'Version', 'VersionDate', 'Gene']
    
    dr_PI=drug_resistance[drug_resistance['DrugClass']=="PI"]
    dr_PI=dr_PI[['DrugDisplayAbbr', 'Score', 'Susceptibility']]
    dr_PI

    dr_NRTI=drug_resistance[drug_resistance['DrugClass']=="NRTI"]
    dr_NRTI=dr_NRTI[['DrugDisplayAbbr', 'Score', 'Susceptibility']]
    dr_NRTI
    
    dr_NNRTI=drug_resistance[drug_resistance['DrugClass']=="NNRTI"]
    dr_NNRTI=dr_NNRTI[['DrugDisplayAbbr', 'Score', 'Susceptibility']]
    dr_NNRTI

    dr_INSTI=drug_resistance[drug_resistance['DrugClass']=="INSTI"]
    dr_INSTI=dr_INSTI[['DrugDisplayAbbr', 'Score', 'Susceptibility']]
    dr_INSTI

    algorithm=drug_resistance['Version'][0] + "(" + drug_resistance['VersionDate'][0] + ")"

    mutations=data[0]['drugResistance']
    #mutations=pd.json_normalize(mutations, record_path=['drugScores','partialScores', 'mutations'])[['text','primaryType']]
    mutations=pd.json_normalize(mutations, record_path=['drugScores','partialScores'], meta=[['drugScores','drugClass','name']],errors='ignore')
    PI_major, PI_accessory, NNRTI_muts, NRTI_muts, INSTI_major, INSTI_accessory=json_normalise_helper(mutations)

    comments=data[0]['drugResistance']
    comments=pd.json_normalize(comments, record_path=['drugScores','partialScores', 'mutations', 'comments'])['text']
    comments=list(set(comments))

    context={'seqName': seqName,
             'subType': subType,
             'genes_ranges': genes_ranges,
             'dr_PI': dr_PI,
             'dr_NRTI': dr_NRTI,
             'dr_NNRTI': dr_NNRTI,
             'dr_INSTI': dr_INSTI,
             'mutations': mutations,
             'PI_major': PI_major, 
             'PI_accessory': PI_accessory, 
             'NNRTI_muts': NNRTI_muts, 
             'NRTI_muts': NRTI_muts, 
             'INSTI_major': INSTI_major, 
             'INSTI_accessory': INSTI_accessory,
             'comments': comments,
             'algorithm':algorithm,
             'time':'None',
             }
    
    #result = generate_pdf('analysis/drug_resistance_report.html', file_object=pdf_resp, context=context)
    #return result
    return render(request, context=context, template_name="analysis/drug_resistance_report.html")