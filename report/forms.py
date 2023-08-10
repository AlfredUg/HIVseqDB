from django import forms  
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout, Submit, Button

class DrugResistanceReportForm(forms.Form):
    Description = forms.CharField(max_length=100)
    JSON_file = forms.FileField()

    @property
    def helper(self):
        helper = FormHelper(self)
        helper.layout=Layout()
        for field in self.Meta().fields:
            helper.layout.append(
                Field(field, wrapper_class='row')
            )
        helper.layout.append(Submit('submit', 'Generate report', css_class='btn-success'))
        helper.layout.append(Button('cancel', 'Cancel', css_class='btn-danger'))
        helper.field_class='col-9'
        helper.label_class='col-3'
        helper.form_class = 'form-horizontal'
        return helper

