from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('fullname','mobile','empcode','country','city','position')
        labels = {
            'fullname' : 'Full Name',
            'mobile' : 'Mobile',
            'empcode' : 'Employee Code',
            'country' : 'Country',
            'city' : 'City',
            'postion': 'Position'
        }


    def __init__(self,*args,**kwargs):
        super(EmployeeForm,self).__init__(*args,**kwargs)
        self.fields['position'].empty_label = "Select Position"  
        self.fields['country'].empty_label = "Select Country"
        self.fields['city'].empty_label = "Select City"  
        self.fields['empcode'].required = False