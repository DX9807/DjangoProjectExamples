from django import forms
#from django.forms import ModelForm
from pages.models import Users,Student

#creating forms with models...
class UsersForm(forms.ModelForm):

    class Meta():
        model=Users
        fields='__all__'


class StudentForm(forms.ModelForm):

    class Meta():
        model=Student
        fields='__all__'
