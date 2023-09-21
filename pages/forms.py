from django import forms
from .models import Student
class StudentRegistration(forms.ModelForm):
    class Meta:
        model=Student
        fields=['name','number','email','subject','message']
        widgets = {
            'name': forms.TextInput(attrs={'id': 'name'}),
            'number': forms.TextInput(attrs={'id': 'number'}),
            'email': forms.TextInput(attrs={'id': 'email' }),
            'subject': forms.TextInput(attrs={'id': 'subject' }),
            'message': forms.TextInput(attrs={'id': 'message' }),
        }
        