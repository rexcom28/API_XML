from dataclasses import fields
from contactforms.models import Contact
from django import forms
from . models import (
    Profile, 
    CustomContact, 
    profileReadeMore, 
    Technology_type,
    profilie_social_media,
    profile_work_images,
)    
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

class CustomContactForm_isRead(forms.ModelForm):
    id = forms.IntegerField(widget=forms.HiddenInput)
    is_readed = forms.BooleanField(required=False)
    class Meta:
        model = CustomContact
        exclude = ('created', 'name', 'email', 'subject', 'message', 'contact_to_user')
        fields =('id','is_readed',)
class CustomContactForm(forms.ModelForm):
    class Meta:
        model = CustomContact
        exclude = ('created','is_readed')
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


class TechsTypesForm_ADD(forms.ModelForm):
    id = forms.IntegerField(widget=forms.HiddenInput,required=False)
    class Meta:
        model = Technology_type
        fields = '__all__'
        labels = {
            'tech':('Technology'),
            'desc':('Description'),
        }
class TechsTypesForm(forms.ModelForm):
    id = forms.IntegerField(widget=forms.HiddenInput)
    class Meta:
        model = Technology_type
        fields = '__all__'
        labels = {
            'tech':('Technology'),
            'desc':('Description'),
        }

class SocialsForm(forms.ModelForm):

    id = forms.IntegerField(widget=forms.HiddenInput,required=False)
    class Meta:
        model  = profilie_social_media
        fields = ('id','social_type', 'url')

class Work_Images_Form(forms.ModelForm):
    id = forms.IntegerField(widget=forms.HiddenInput,required=False)
    class Meta:
        model = profile_work_images
        fields  = '__all__'
        exclude =('profile',)