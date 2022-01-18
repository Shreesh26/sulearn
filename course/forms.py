from django import forms
from .models import *

class CustomMMCF(forms.ModelMultipleChoiceField):
    def label_from_instance(self, subject):
        return '%s' %subject.area

class teacher_form(forms.ModelForm):
    dob=forms.DateField(widget=forms.DateInput(format=('%d-%m-%Y'), 
                               attrs={'class':'myDateClass', 
                               'placeholder':'Select a date'}
    ),
    )
    city=forms.CharField(widget=forms.TextInput(attrs={ "placeholder":"Enter the You live in", 'class':"form-control", 'id':"city",}
    ),
    )
    state=forms.CharField(widget=forms.TextInput(attrs={ "placeholder":"Enter the state you live in", 'class':"form-control", 'id':"state",}
    ),
    )
    about=forms.CharField(widget=forms.Textarea(attrs={ "placeholder":"Tell us about yourself. Be sure to include your educational qualifications,as this will be published in your educators profile", 'class':"form-control", 'id':"about",}
    ),
    )
    class Meta:
        model=teacher_app
        fields=['dob', 'city', 'state', 'about']


class courseForm(forms.ModelForm):
    title=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Enter the Course Title", "class":"form-control", "id":'title'}
    ),
    )
    areas=forms.ModelMultipleChoiceField(queryset=subject.objects.all(), widget=forms.CheckboxSelectMultiple),
    description=forms.CharField(widget=forms.Textarea(attrs={ "placeholder":"Tell us about the course", 'class':"form-control", 'id':"about",}
    ),
    )
    material=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Enter the URL where you have uploaded the course material", "class":"form-control", "id":'material'}
    ),
    )
    class Meta:
        model=course
        fields=['title','areas', 'description', 'material']
