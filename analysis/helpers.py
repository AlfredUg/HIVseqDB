from analysis.models import  AnalysisResults, NewAnalysis, MinorityVariantsResult
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
        project_ID=NewAnalysis.objects.get(project_ID=row['project_ID']), #take note of how to handle foreign keys in django
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