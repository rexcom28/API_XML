from django import template
from django.contrib.auth.models import Permission
from django.urls import reverse
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.files import File


register = template.Library()


@register.simple_tag
def exist(user):
    ruta2 = ['Profiles','assets','css',f'{user}.css']
    global nfile
    nfile = settings.STATICFILES_DIRS[0]
    store  = FileSystemStorage(location=settings.STATICFILES_DIRS[0])
    for i in ruta2:
            nfile = os.path.join(nfile,i)
    if not store.exists(nfile):
        return True
    else:
        return False
@register.simple_tag
def userCssFile(user,url):
    #print(url)
    #print(user)
    full = f'/{url}{user}.css'
    return full

@register.filter
def modulo(num, val):
    return num % val

@register.simple_tag
def tab_name(field):
    name = field.replace('_', ' ')
    return name.capitalize()

@register.simple_tag
def num_permissions(permissons_fields,model):
    permissons_fields.field.queryset = Permission.objects.all().filter(content_type__model=model)
    return permissons_fields
@register.simple_tag
def num_edit_permissions(perm,model):
    lis = []
    for i in perm:
        if model == i.data['label'].split('|')[1].replace(' ',''):
            #print(i.data)
            lis.append(i)
    return lis

@register.simple_tag
def trim_field_name(field):
    #print(dir(field.choice_label))
    #rp =field.choice_label.split('|')[2] 
    #del field.choice_label
    return field

@register.simple_tag
def num_tabs_():
    lis = []
    permissions =Permission.objects.filter(content_type__app_label='Profiles').values('content_type__model').distinct()
    for i in permissions:
        if i['content_type__model'] not in lis:
            lis.append(i['content_type__model'])
    return lis

@register.simple_tag
def num_tabs_edit(qs):
    lis = []
    if qs =="":
        permissions =Permission.objects.filter(content_type__app_label='Profiles').values('content_type__model').distinct()
    else:
        permissions = Permission.objects.filter(content_type__app_label=qs).values('content_type__model').distinct()
    for i in permissions:
        if i['content_type__model'] not in lis:
            lis.append(i['content_type__model'])
    return lis

@register.simple_tag
def is_actual_path(path,url):
    return "active" if path == reverse(url) else ""
        