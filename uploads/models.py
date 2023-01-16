from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
def project_upload_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / ngs/<projectName>/<filename>
    return 'ngs/projects/{0}/{1}'.format(instance.project_Name, filename)

class Project(models.Model):
    project_ID=models.AutoField(primary_key=True)
    project_Name=models.CharField(max_length=50)
    Region_Sequenced=models.CharField(max_length=50)
    Sequencing_Technology=models.CharField(max_length=50)
    Sequencing_Platform=models.CharField(max_length=50)
    Sequencing_Date=models.DateField(default=timezone.now)
    fastq_File = models.FileField(upload_to=project_upload_path, blank=True, null=True)
    def get_absolute_url(self):
        return reverse('newAnalysisForm')

class SampleFile(models.Model):
    sample_File = models.FileField(blank=True, null=True)



class Tasks(models.Model):
    task_id = models.CharField(max_length=50)
    job_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.task_id} {self.job_name}'
