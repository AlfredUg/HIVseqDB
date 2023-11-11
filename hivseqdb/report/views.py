from django.shortcuts import render, redirect
from django.views import generic

import os
import json
from django.conf import settings
import pandas as pd
from analysis.helpers import json_normalise_helper
from report.forms import DrugResistanceReportForm

# Create your views here.

class DrugResistanceView(generic.View):
    
    def get(self, request, *args, **kwargs):
        form = DrugResistanceReportForm()
        return render(request, 'report/upload-json.html', {'form': form})
    
    def post(self, request, *args, **kwargs):
        # Doing something with the POST data
        if request.method == 'POST':
            form = DrugResistanceReportForm(request.POST, request.FILES)
            if form.is_valid():
                report_data=drug_resistance_report(request.FILES['JSON_file'])
                return redirect('reportResult', report_data=report_data)

def drug_report_page(request, **kwargs):
    context = {}
    if 'report_data' in kwargs:
        context = kwargs['report_data']
    return render(request, template_name='analysis/drug_resistance_report.html', context=context)

# def drug_resistance_tool(request):
#     if request.method == 'POST':
#         form = DrugResistanceReportForm(request.POST, request.FILES)
#         if form.is_valid():
#             report_data=drug_resistance_report(request.FILES['JSON_file'])
#             return redirect("reportResult", report_data=report_data)
#     else:
#         form = DrugResistanceReportForm()
#         return render(request, 'report/upload-json.html', {'form': form})

def drug_resistance_report(json_report_path):
        
        json_report = open(json_report_path)
        data = json.load(json_report)
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
        
        return context