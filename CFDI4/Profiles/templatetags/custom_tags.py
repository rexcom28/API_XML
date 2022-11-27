from django import template
from django.contrib.auth.models import Permission
from django.urls import reverse
register = template.Library()

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
        