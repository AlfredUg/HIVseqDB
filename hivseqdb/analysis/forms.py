from django import forms  
from django.forms import ModelForm
from analysis.models import NewAnalysis  
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout, Submit, Button  

class NewAnalysisForm(ModelForm):
    class Meta:  
            model = NewAnalysis  
            fields = ['project_ID',  'description', 
                     'email', 'consensus_Percentage', 'error_Rate', 
                     'length_Cutoff', 'minimum_Allele_Count', 
                     'minimum_Mutation_Frequency', 'minimum_Read_Depth', 
                     'minimum_Variant_Quality', 'mutation_Database', 'score_Cutoff',
                    'target_Coverage']

            widgets = {
            'email': forms.EmailInput()
        }   
    
    @property
    def helper(self):
        helper = FormHelper(self)
        helper.layout=Layout()
        for field in self.Meta().fields:
            helper.layout.append(
                Field(field, wrapper_class='row')
            )
        helper.layout.append(Submit('submit', 'Submit analysis', css_class='btn-success'))
        helper.layout.append(Button('cancel', 'Cancel', css_class='btn-danger'))
        helper.field_class='col-9'
        helper.label_class='col-3'
        helper.form_class = 'form-horizontal'
        return helper