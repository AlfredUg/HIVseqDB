from analysis.models import  AnalysisResults, NewAnalysis, MinorityVariantsResult

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