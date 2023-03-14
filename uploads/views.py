from django.views import generic
from django.http import HttpResponseRedirect
from uploads.models import Project, Sample
from uploads.forms import DataUploadForm
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
import pandas as pd

# Create your views here.

from uploads.tasks import process
from uploads.models import Tasks
#from celery.result import AsyncResult

class CreateDataUpload(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    template_name = 'uploads/upload-NGS-data.html'
    form_class = DataUploadForm

    def post(self, *args, **kwargs):
          form = DataUploadForm(data=self.request.POST, files=self.request.FILES)      
          if form.is_valid():
              projectName=self.request.POST['project_Name']
              Region_Sequenced=self.request.POST['Region_Sequenced']
              Sequencing_Platform=self.request.POST['Sequencing_Platform']
              Sequencing_Date=self.request.POST['Sequencing_Date']
              sample_file=self.request.FILES['sample_File']
              df=pd.read_csv(sample_file, delimiter=',')
              print(df)
              
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
              
              for file in self.request.FILES.getlist('fastq_Files'):
                project_instance = Project(
                    fastq_Files=file, 
                    project_Name=projectName,
                    Region_Sequenced=Region_Sequenced,
                    Sequencing_Platform=Sequencing_Platform,
                    Sequencing_Date=Sequencing_Date)
                project_instance.save()
              
              messages.success(self.request, 'Congrats! Your data submission was successful')
              
              return HttpResponseRedirect(self.request.path_info)