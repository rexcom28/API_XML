from .models import CSSConf
from django import forms

class CSSConf_Form(forms.ModelForm):

    class Meta:
        model = CSSConf
        fields = ('user','fondo','backColor', 'fontColor',)
        widgets ={
            'user': forms.HiddenInput(),
            
            'fondo': forms.ClearableFileInput(attrs={
                'class':'image rounded',
                "height":"200px",     
                "required": False,           
            }),
            'backColor':forms.HiddenInput(),
            'fontColor':forms.HiddenInput(),
        }