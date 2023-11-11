from django.shortcuts import render
from django.contrib import messages

# Create your views here.

def home(request):
    messages.info(request,'Welcome to HIVseqDB, store data, analyse data, browse data and analyses.')
    # messages.warning(request,
    # 'This instance only allows browsing of already analysed data. '+
    # 'To upload and analyse own data, kindly install an instance as indicated in the documentation.')
    # messages.info(request, 
    # 'NOTE: The NGS data used in this demonstration is publically available at the NCBI Sequence Read Archive (SRA)'+
    # 'and the European Nucleotide Archive (ENA), Bioproject accession PRJNA340290.'+ 
    # 'Corresponding sample data was obtained from the associated publication. Many thanks to Avila-Ríos, Santiago, et al. "HIV drug resistance in antiretroviral treatment-naïve individuals in the largest public hospital in Nicaragua, 2011-2015." PLoS One 11.10 (2016): e0164156.') 

    return render(request, 'base/home.html')

def login(request):
    return render(request, 'base/login.html')