from dataclasses import fields
from contactforms.models import Contact
from django import forms
from . models import Profile, CustomContact, profileReadeMore
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ( 'first_name', 'last_name', 'email',)

class ProfileForm(forms.ModelForm):
    #birthdate = forms.DateField()
    #avatar = forms.FileInput(required =False)
    class Meta:
        model = Profile
        fields = ('bio', 'avatar', 'job_title', 'good_at_bio', 'mywork_bio', 'contact_msn', 'show_socials', 'show_ReadMore', 'show_GoodAt', 'show_WorkImages')            
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
    
class ProfileReadMoreForm(forms.ModelForm):
    id = forms.IntegerField(widget=forms.HiddenInput)
    class Meta:
        model = profileReadeMore
        fields = ('id','title', 'description', 'section_type', 'left_rigth', 'image',)
class ProfileReadMore_AddForm(forms.ModelForm):
    class Meta:
        model = profileReadeMore
        fields = ('title', 'description', 'section_type', 'left_rigth', 'image',)

class CustomContactForm(forms.ModelForm):
    class Meta:
        model = CustomContact
        exclude = ('created',)
        labels = {
            'contact_to_user':(''),
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message'}),
            'contact_to_user': forms.Select(attrs={'class': 'input-group-field', 'style':'display:none'}),

        }