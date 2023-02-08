from django.views import generic
from django.http import HttpResponseRedirect
from uploads.models import Project
from uploads.forms import FastqUploadForm, SampleDataUploadForm
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

from uploads.tasks import process
from uploads.models import Tasks
#from celery.result import AsyncResult

class CreateFastqUpload(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    template_name = 'uploads/upload-NGS-data.html'
    form_class = FastqUploadForm

    def post(self, *args, **kwargs):
          form = FastqUploadForm(data=self.request.POST, files=self.request.FILES)      
          if form.is_valid():
              projectName=self.request.POST['project_Name']
              Region_Sequenced=self.request.POST['Region_Sequenced']
              Sequencing_Platform=self.request.POST['Sequencing_Platform']
              Sequencing_Date=self.request.POST['Sequencing_Date']
              for file in self.request.FILES.getlist('fastq_File'):
                  project_instance = Project(fastq_File=file, 
                                          project_Name=projectName,
                                          Region_Sequenced=Region_Sequenced,
                                          Sequencing_Platform=Sequencing_Platform,
                                          Sequencing_Date=Sequencing_Date
                                          )
                  project_instance.save()
              messages.success(self.request, 'Congrats! Your data submission was successful')
              return HttpResponseRedirect(self.request.path_info)
                
class CreateSampleUpload(generic.CreateView):
    template_name = 'uploads/upload-sample-metadata.html'
    form_class = SampleDataUploadForm
