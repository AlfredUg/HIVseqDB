from django import forms  
from django.forms import ModelForm
from search.models import Sample  
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout, HTML, Submit, Button  

class AdvancedSearchForm(ModelForm):
    class Meta:  
            model = Sample  
            fields = '__all__'

            widgets = {
            'email': forms.EmailInput()
        }   
    
    @property
    def helper(self):
        helper = FormHelper(self)
        for field in self.Meta().fields:
            helper.layout.append(
                Field(field, wrapper_class='row')
            )
        helper.layout.append(Submit('submit', 'Submit analysis', css_class='btn-success'))
        helper.field_class='col-8'
        helper.label_class='col-3'
        helper.form_class = 'form-horizontal'
        return helper