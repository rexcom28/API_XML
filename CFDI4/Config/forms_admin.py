from django import forms
from django.contrib.auth.models import Group,User,Permission
from django.contrib.contenttypes.models import ContentType

class GroupForm(forms.ModelForm):    
    permissions = forms.ModelMultipleChoiceField(queryset= Permission.objects.all().filter(content_type__app_label='Profiles'), widget  = forms.CheckboxSelectMultiple)
    
    def __init__(self,*args,**kwargs):
        qs=kwargs.pop('qs', None)
        
        super(GroupForm,self).__init__(*args,**kwargs)
        if qs:        
            self.fields['permissions']  = forms.ModelMultipleChoiceField(queryset= qs,widget  = forms.CheckboxSelectMultiple)
    class Meta:
        model   = Group
        fields  = ('name', 'permissions',)

    

    


