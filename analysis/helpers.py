from analysis.models import  AnalysisResults, NewAnalysis, MinorityVariantsResult
from uploads.models import Sample
import pandas as pd
import numpy as np

def update_analysis_results(df):
    for index, row in df.iterrows():
        AnalysisResults.objects.update_or_create(
        sample_ID=row['sample_ID'],
        drugClass=row['drugClass'],
        drugName=row['drugName'],
        drugScore=row['drugScore'], 
        susceptibility=row['susceptibility'],
        project_ID=row['project_ID']#NewAnalysis.objects.get(project_ID=row['project_ID']), #take note of how to handle foreign keys in django
        )

def update_minority_variants(df):
    for index, row in df.iterrows():
        MinorityVariantsResult.objects.update_or_create(
            chromosome=row['chromosome'],
            gene=row['gene'],
            category=row['category'],
            surveillance=row['surveillance'], 
            wildtype=row['wildtype'],
            position=row['position'],
            mutation=row['mutation'], 
            mutation_frequency=row['mutation_frequency'],
            coverage=row['coverage'],
            sample=row['sample'],
            project=row['project'] #take note of how to handle foreign keys in django
        )

# function to create highcharts

def project_gene_drms(project, gene):
    variants=MinorityVariantsResult.objects.filter(project=project, gene=gene)
    pdmv = pd.DataFrame.from_records(variants.values())
    pdmv['variant']=pdmv['wildtype']+pdmv['position'].astype(str)+pdmv['mutation']
    pdmv['frequency'] = np.where(pdmv['mutation_frequency']>=20, 'High abundant variants', 'Low-abundant variants')
    #pdmv=pdmv.groupby(["frequency", "variant"])["result"].count().reset_index(name="count")
    pdmv=pdmv.groupby(['frequency','variant'])["result"].count().reset_index(name="count").pivot('variant','frequency').fillna(0)
    print(pdmv.head())
    variants = list(pdmv.index.values)
    majority = list(pdmv['count']['High abundant variants'])
    minority = list(pdmv['count']['Low-abundant variants'])
    chart_data = [variants, majority, minority]
    return chart_data

def sample_gene_drms(sample, gene):
    
    variants=MinorityVariantsResult.objects.filter(sample=sample, gene=gene)
    sample_df = pd.DataFrame.from_records(Sample.objects.filter(sampleName=sample).values())
    variants_df=pd.DataFrame.from_records(variants.values())

    pdmv = pd.merge(sample_df,variants_df, left_on='sampleName', right_on='sample')
    
    #change the next line to mutational load
    pdmv['coverage'] = pdmv['viralLoad'].multiply(pdmv['mutation_frequency'],axis="index")

    pdmv['variant']=pdmv['wildtype']+pdmv['position'].astype(str)+pdmv['mutation']
    
    tmp = pdmv[['category', 'variant', 'mutation_frequency', 'coverage']]

    minor=[]
    minor_freq=[]
    minor_cov=[]

    major=[]
    major_freq=[]
    major_cov=[]

    if gene=='PR':
        minor=list(tmp[tmp['category']=='PIMinor']['variant'])
        minor_freq=list(tmp[tmp['category']=='PIMinor']['mutation_frequency'].astype(float))
        minor_cov=list(tmp[tmp['category']=='PIMajor']['coverage'].astype(float)) # we report coverage in thousands

        major=list(tmp[tmp['category']=='PIMajor']['variant'])
        major_freq=list(tmp[tmp['category']=='PIMajor']['mutation_frequency'].astype(float))
        major_cov=list(tmp[tmp['category']=='PIMajor']['coverage'].astype(float)) # we report coverage in thousands

    elif gene=='RT':
        minor=list(tmp[tmp['category']=='NNRTI']['variant'])
        minor_freq=list(tmp[tmp['category']=='NNRTI']['mutation_frequency'].astype(float))
        minor_cov=list(tmp[tmp['category']=='NNRTI']['coverage'].astype(float)) # we report coverage in thousands

        major=list(tmp[tmp['category']=='NRTI']['variant'])
        major_freq=list(tmp[tmp['category']=='NRTI']['mutation_frequency'].astype(float))
        major_cov=list(tmp[tmp['category']=='NRTI']['coverage'].astype(float)) # we report coverage in thousands
    
    chart_data=[variants, major, major_freq, major_cov, minor, minor_freq, minor_cov]

    return chart_data

def check_string(x):
    if x=='':
        x='None'
    else:
        x=x
    return x

def json_normalise_helper(mutations):
    df_mat = np.zeros(shape=(0,3))
    
    for i in range(0, mutations.shape[0]):

        m2 = mutations.iloc[i]
        dc = m2['drugScores.drugClass.name']
        
        m3 = list(m2['mutations'])
        
        for j in range(0, len(m3)):
            
            mut = m3[j]['text']
            category = m3[j]['primaryType']
            
            df_mat = np.append(df_mat, [[mut, dc, category]], axis=0)

    df_mat_2 = pd.DataFrame(df_mat, columns = ['Mutation','Drugclass','Category'])

    PI_major, PI_accessory, NNRTI_muts, NRTI_muts, INSTI_major, INSTI_accessory = None,None,None,None,None,None
    
    PI = df_mat_2[df_mat_2['Drugclass']=="PI"]
    PI_major = set(PI[PI['Category']=="Major"]["Mutation"])
    PI_major=check_string(', '.join(PI_major))

    PI_accessory = set(PI[PI['Category']=="Accessory"]["Mutation"])
    PI_accessory=check_string(', '.join(PI_accessory))

    NNRTI_muts = set(df_mat_2[df_mat_2['Drugclass']=="NNRTI"]["Mutation"])
    NNRTI_muts=check_string(', '.join(NNRTI_muts))

    NRTI_muts = set(df_mat_2[df_mat_2['Drugclass']=="NRTI"]["Mutation"])
    NRTI_muts=check_string(', '.join(NRTI_muts))

    INSTI = df_mat_2[df_mat_2['Drugclass']=="INSTI"]
    INSTI_major = set(INSTI[INSTI['Category']=="Major"]["Mutation"])
    INSTI_major=check_string(', '.join(INSTI_major))

    INSTI_accessory = set(INSTI[INSTI['Category']=="Accessory"]["Mutation"])
    INSTI_accessory=check_string(', '.join(INSTI_accessory))

    return PI_major, PI_accessory, NNRTI_muts, NRTI_muts, INSTI_major, INSTI_accessory