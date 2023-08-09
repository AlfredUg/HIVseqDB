from django.conf import settings
import subprocess
import os
import pandas as pd
from celery import shared_task
from analysis.helpers import update_analysis_results, update_minority_variants

@shared_task
def run_quasiflow(project):
    """ 
    This function takes up a project ID as input,
    it gets the path to the data of a corresponding project ID,
    similarly, it gets/creates the path for storing analysis results of the project,
    Initiates the HIVDR analysis and updates the database with analysis results
    """
    input=os.path.join(settings.MEDIA_ROOT,'ngs/projects/', project)
    output=os.path.join(settings.MEDIA_ROOT,'ngs/analyses/', project)
    #input=os.path.join(settings.BASE_DIR, 'media/ngs/projects/', project)
    #output=os.path.join(settings.BASE_DIR,'media/ngs/analyses/', project)
    if not os.path.exists(output):
        os.makedirs(output)
    cmd=os.path.join(settings.BASE_DIR, 'scripts/runHIVDRanalysis.sh')
    subprocess.run(["sh", cmd, input, output])
    update_results(projectID=project)
    update_minority(projectID=project)
    return True

@shared_task
def update_minority(projectID):
    """
    This function takes the project ID,
    creates a path to corresponding analysis results,
    reads the analysis results of that particular project,
    uses a helper function to update the database with analysis results. 
    """
    report_path=os.path.join(settings.BASE_DIR,'media/ngs/analyses/',projectID,'combined_minority_variants_report.csv')
    df=pd.read_csv(report_path, delimiter=',')
    df.columns=['chromosome', 'gene', 'category', 'surveillance', 'wildtype',
                'position', 'mutation', 'mutation_frequency', 'coverage', 'sample']
    df['project']=projectID
    # df['sample']='None'
    print(df)
    update_minority_variants(df) 
    return True

@shared_task
def update_results(projectID):
    """
    This function takes the project ID,
    creates a path to corresponding analysis results,
    reads the analysis results of that particular project,
    uses a helper function to update the database with analysis results. 
    """
    report_path=os.path.join(settings.BASE_DIR,'media/ngs/analyses/',projectID,'combined_hivdr_report.csv')
    df=pd.read_csv(report_path, delimiter=',')
    df.columns=['drugClass', 'drugName', 'drugScore', 'susceptibility', 'sample_ID']
    df['project_ID']=projectID
    print(df)
    update_analysis_results(df) 
    return True