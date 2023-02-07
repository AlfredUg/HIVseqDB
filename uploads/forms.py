from django import forms
from django.forms import ModelForm
from uploads.models import Project,SampleFile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout, HTML, Submit, Button 

class SampleDataUploadForm(ModelForm):
    class Meta:  
            model = SampleFile  
            fields = ['sample_File']
            widget = { 'sample_File': forms.FileInput(
            attrs={'class': 'form-control', 
            'placeholder': 'Upload "participant.csv"', 
            'help_text': 'Choose a participant.csv file'})}
    
    @property
    def helper(self):
        helper = FormHelper(self)
        helper.layout=Layout()
        for field in self.Meta().fields:
            helper.layout.append(
                Field(field, wrapper_class='row')
            )
        helper.layout.append(Submit('submit', 'Submit analysis', css_class='btn-success'))
        helper.field_class='col-9'
        helper.label_class='col-3'
        helper.form_class = 'form-horizontal'
        helper.layout.append(Button('cancel', 'Cancel', css_class='btn-danger'))
        return helper

class FastqUploadForm(ModelForm):
    class Meta:  
            model = Project  
            fields = ['project_Name',
                    'Region_Sequenced',
                    'Sequencing_Platform',
                    'Sequencing_Date',
                    'fastq_File']
            platforms=(
                ('Illumina MiSeq', 'Illumina MiSeq'),
                ('Illumina NextSeq', 'Illumina NextSeq'),
                ('Illumina NovaSeq', 'Illumina NovaSeq')  
            )
            regions=(
                ('Integrase', 'Integrase'),
                ('Reverse Transcriptase', 'Reverse Transcriptase'),
                ('Protease and Reverse Transcriptase', 'Protease and Reverse Transcriptase'),  
                ('Near Full Length', 'Near Full Length')  
            )
            widgets = {
                'fastq_File': forms.ClearableFileInput(attrs={'multiple': True}),
                'Region_Sequenced': forms.Select(choices=regions),
                'Sequencing_Platform': forms.Select(choices=platforms), 
                'Sequencing_Date': forms.DateInput(attrs={'type': 'date'}),               
            }  
    
    @property
    def helper(self):
        helper = FormHelper(self)
        helper.layout=Layout()        
        for field in self.Meta().fields:
            helper.layout.append(
                Field(field, wrapper_class='row')
            )
        helper.layout.append(Submit('submit', 'Submit', css_class='btn-success'))
        helper.layout.append(Button('reset', 'Cancel', css_class='btn-danger'))
        helper.field_class='col-9'
        helper.label_class='col-3'
        helper.form_class = 'form-horizontal'
        return helper