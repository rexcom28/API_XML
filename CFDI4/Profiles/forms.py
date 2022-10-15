from django.forms.models import inlineformset_factory
from django import forms
from . models import Profile
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)

class ProfileForm(forms.ModelForm):
    #birthdate = forms.DateField()
    #avatar = forms.FileInput(required =False)
    class Meta:
        model = Profile
        fields = ('bio', 'avatar',)            
        widgets = {
            'bio': forms.Textarea(attrs={
                'rows':3,
                'class': 'form-control',
                'id':'bio',
                'placeholder':'bio',
            }),
            'avatar':forms.ClearableFileInput(attrs={
                'class':'image rounded',
                "height":"200px",     
                "required": False,           
            }),
        }
    
