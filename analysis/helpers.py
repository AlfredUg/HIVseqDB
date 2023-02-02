from analysis.models import  AnalysisResults, NewAnalysis

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