from django import forms
from django.forms import ModelForm
from uploads.models import Project, ConsensusSequence
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout, Submit, Button 

class DataUploadNGSBatchForm(ModelForm):
    class Meta:  
            model = Project  
            fields = ['project_Name',
                    'Region_Sequenced',
                    'Sequencing_Platform',
                    'sample_CSV_File',
                    'fastq_Files']
            platforms=(
                ('Illumina MiSeq', 'Illumina MiSeq'),
                ('Illumina NextSeq', 'Illumina NextSeq'),
                ('Illumina NovaSeq', 'Illumina NovaSeq'),
                ('Sanger', 'Sanger'),  
                ('Oxford Nanopore MiniIon', 'Oxford Nanopore MiniIon'),  
                ('PacBio', 'PacBio')  
            )
            regions=(
                ('Integrase', 'Integrase'),
                ('Reverse Transcriptase', 'Reverse Transcriptase'),
                ('Protease and Reverse Transcriptase', 'Protease and Reverse Transcriptase'),  
                ('Near Full Length', 'Near Full Length'),
                ('Env', 'Env'),
                ('Pol', 'Pol'),
                ('Gag', 'Gag') 
            )
            widgets = {
                'fastq_Files': forms.ClearableFileInput(attrs={'multiple': True}),
                'Region_Sequenced': forms.Select(choices=regions),
                'Sequencing_Platform': forms.Select(choices=platforms), 
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
    
class DataUploadSingleForm(ModelForm):
    class Meta:  
            model = Project  
            fields = ['project_Name',
                    'Region_Sequenced',
                    'Sequencing_Platform',
                    'sample_CSV_File',
                    'fastq_Files']
            platforms=(
                ('Illumina MiSeq', 'Illumina MiSeq'),
                ('Illumina NextSeq', 'Illumina NextSeq'),
                ('Illumina NovaSeq', 'Illumina NovaSeq'),
                ('Sanger', 'Sanger'),  
                ('Oxford Nanopore MiniIon', 'Oxford Nanopore MiniIon'),  
                ('PacBio', 'PacBio')  
            )
            regions=(
                ('Integrase', 'Integrase'),
                ('Reverse Transcriptase', 'Reverse Transcriptase'),
                ('Protease and Reverse Transcriptase', 'Protease and Reverse Transcriptase'),  
                ('Near Full Length', 'Near Full Length'),
                ('Env', 'Env'),
                ('Pol', 'Pol'),
                ('Gag', 'Gag') 
            )
            widgets = {
                'fastq_Files': forms.ClearableFileInput(attrs={'multiple': True}),
                'Region_Sequenced': forms.Select(choices=regions),
                'Sequencing_Platform': forms.Select(choices=platforms), 
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
    
class DataUploadConsensusBatchForm(ModelForm):
    class Meta:  
            model = ConsensusSequence  
            fields = ['project_Name',
                    'Region_Sequenced',
                    'Sequencing_Platform',
                    'sample_CSV_File',
                    'fasta_File']
            platforms=(
                ('Illumina MiSeq', 'Illumina MiSeq'),
                ('Illumina NextSeq', 'Illumina NextSeq'),
                ('Illumina NovaSeq', 'Illumina NovaSeq'),
                ('Sanger', 'Sanger'),  
                ('Oxford Nanopore MiniIon', 'Oxford Nanopore MiniIon'),  
                ('PacBio', 'PacBio')  
            )
            regions=(
                ('Integrase', 'Integrase'),
                ('Reverse Transcriptase', 'Reverse Transcriptase'),
                ('Protease and Reverse Transcriptase', 'Protease and Reverse Transcriptase'),  
                ('Near Full Length', 'Near Full Length'),
                ('Env', 'Env'),
                ('Pol', 'Pol'),
                ('Gag', 'Gag') 
            )
            widgets = {
                'fasta_File': forms.ClearableFileInput(attrs={'multiple': True}),
                'Region_Sequenced': forms.Select(choices=regions),
                'Sequencing_Platform': forms.Select(choices=platforms), 
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