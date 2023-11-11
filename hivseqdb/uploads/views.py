from django.views import generic
from django.http import HttpResponseRedirect
from uploads.forms import DataUploadNGSBatchForm, DataUploadSingleForm, DataUploadConsensusBatchForm
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
import pandas as pd
from uploads.tasks import populate_samples, populate_fastq_files
from uploads.models import Project, Sample

# Create your views here.

class CreateDataUpload(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    template_name = 'uploads/batch-upload-ngs.html'
    form_class = DataUploadNGSBatchForm

    def post(self, *args, **kwargs):
          form = DataUploadNGSBatchForm(data=self.request.POST, files=self.request.FILES)      
          if form.is_valid():
              projectName=self.request.POST['project_Name']
              Region_Sequenced=self.request.POST['Region_Sequenced']
              Sequencing_Platform=self.request.POST['Sequencing_Platform']
              sample_file=self.request.FILES['sample_CSV_File']
              
              df=pd.read_csv(sample_file, delimiter=',')
              print(df)
              #populate_samples.delay(df, projectName)
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
              
              #populate_fastq_files.delay(fastqFiles, projectName, Region_Sequenced, Sequencing_Platform, Sequencing_Date)
              for file in self.request.FILES.getlist('fastq_Files'):
                project_instance = Project(
                    fastq_Files=file, 
                    project_Name=projectName,
                    Region_Sequenced=Region_Sequenced,
                    Sequencing_Platform=Sequencing_Platform)
                project_instance.save()
              messages.success(self.request, 'Congrats! Your data submission was successful')
              
              return HttpResponseRedirect(self.request.path_info)
          
class CreateDataUploadSingle(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    template_name = 'uploads/single-upload-ngs.html'
    form_class = DataUploadNGSBatchForm

    def post(self, *args, **kwargs):
          form = DataUploadNGSBatchForm(data=self.request.POST, files=self.request.FILES)      
          if form.is_valid():
              projectName=self.request.POST['project_Name']
              Region_Sequenced=self.request.POST['Region_Sequenced']
              Sequencing_Platform=self.request.POST['Sequencing_Platform']
              sample_file=self.request.FILES['sample_CSV_File']
              
              df=pd.read_csv(sample_file, delimiter=',')
              print(df)
              #populate_samples.delay(df, projectName)
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
              
              #populate_fastq_files.delay(fastqFiles, projectName, Region_Sequenced, Sequencing_Platform, Sequencing_Date)
              for file in self.request.FILES.getlist('fastq_Files'):
                project_instance = Project(
                    fastq_Files=file, 
                    project_Name=projectName,
                    Region_Sequenced=Region_Sequenced,
                    Sequencing_Platform=Sequencing_Platform)
                project_instance.save()

              messages.success(self.request, 'Congrats! Your data submission was successful')
              
              return HttpResponseRedirect(self.request.path_info)
          

class CreateDataUploadConsensusSingle(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    template_name = 'uploads/single-upload-consensus.html'
    form_class = DataUploadSingleForm

    def post(self, *args, **kwargs):
          form = DataUploadSingleForm(data=self.request.POST, files=self.request.FILES)      
          if form.is_valid():
              projectName=self.request.POST['project_Name']
              Region_Sequenced=self.request.POST['Region_Sequenced']
              Sequencing_Platform=self.request.POST['Sequencing_Platform']
              sample_file=self.request.FILES['sample_CSV_File']
              
              df=pd.read_csv(sample_file, delimiter=',')
              print(df)
              #populate_samples.delay(df, projectName)
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
            
              messages.success(self.request, 'Congrats! Your data submission was successful')
              
              return HttpResponseRedirect(self.request.path_info)
          
class CreateDataUploadConsensusBatch(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    template_name = 'uploads/batch-upload-consensus.html'
    form_class = DataUploadConsensusBatchForm

    def post(self, *args, **kwargs):
          form = DataUploadConsensusBatchForm(data=self.request.POST, files=self.request.FILES)      
          if form.is_valid():
              projectName=self.request.POST['project_Name']
              Region_Sequenced=self.request.POST['Region_Sequenced']
              Sequencing_Platform=self.request.POST['Sequencing_Platform']
              sample_file=self.request.FILES['sample_CSV_File']
              
              df=pd.read_csv(sample_file, delimiter=',')
              print(df)
              #populate_samples.delay(df, projectName)
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
              
              messages.success(self.request, 'Congrats! Your data submission was successful')
              
              return HttpResponseRedirect(self.request.path_info)