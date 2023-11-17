from django.db import models
from django.utils import timezone
from django.urls import reverse
import os 

# Create your models here.
def project_upload_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / ngs/<projectName>/<filename>
    return 'ngs/projects/{0}/{1}'.format(instance.project_Name, filename)

class Project(models.Model):
    projectID=models.AutoField(primary_key=True)
    project_Name=models.CharField(max_length=50)
    Region_Sequenced=models.CharField(max_length=50)
    Sequencing_Technology=models.CharField(max_length=50)
    Sequencing_Platform=models.CharField(max_length=50)
    fastq_Files = models.FileField(upload_to=project_upload_path, blank=False, null=False)
    sample_CSV_File = models.FileField(blank=False, null=False)

    def filename(self):
        return os.path.basename(self.fastq_Files.path)

    def filesize(self):
        size=os.path.getsize(self.fastq_Files.path) / (1024 * 1024)
        return round(size,2)

    def samplename(self):
        file_name=os.path.basename(self.fastq_Files.name)
        return os.path.splitext(file_name)[0]

    def get_absolute_url(self):
        return reverse('newAnalysisForm')

class Sample(models.Model):
    sample=models.AutoField(primary_key=True)
    sampleName=models.CharField(max_length=250, unique=True)
    samplingDate=models.DateField()
    viralLoad=models.DecimalField(decimal_places=1,max_digits=10)
    cd4=models.DecimalField(decimal_places=1,max_digits=10)
    
    gender=models.CharField(max_length=250)
    age=models.IntegerField()
    literacy=models.CharField(max_length=250)
    employment=models.CharField(max_length=250)
    riskFactors=models.CharField(max_length=250)
    maritalStatus=models.CharField(max_length=250)

    regimen=models.CharField(max_length=250)
    regimenStart=models.DateField()
    
    project=models.CharField(max_length=250)

class Tasks(models.Model):
    task_id = models.CharField(max_length=50)
    job_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.task_id} {self.job_name}'
