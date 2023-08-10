from celery import shared_task
from uploads.models import Project, Sample

@shared_task
def populate_samples(df, projectName):
    for index, row in df.iterrows():
        sampleInstance=Sample(
            sampleName=row['sampleName'],
            samplingDate=row['samplingDate'],
            viralLoad=row['viralLoad'],
            cd4=row['cd4'],
            gender=row['gender'],
            age=row['age'],
            literacy=row['literacy'],
            employment=row['employment'],
            riskFactors=row['riskFactors'],
            maritalStatus=row['maritalStatus'],
            regimen=row['regimen'],
            regimenStart=row['regimenStart'],
            project=projectName)
        sampleInstance.save()
    return True

@shared_task
def populate_fastq_files(fastqFiles, projectName, Region_Sequenced, Sequencing_Platform, Sequencing_Date):
    for file in fastqFiles:
        project_instance = Project(
            fastq_Files=file, 
            project_Name=projectName,
            Region_Sequenced=Region_Sequenced,
            Sequencing_Platform=Sequencing_Platform,
            Sequencing_Date=Sequencing_Date)
        project_instance.save()
    return True