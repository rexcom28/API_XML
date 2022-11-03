from django.http import Http404
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import Group,User, Permission
from django.contrib.contenttypes.models import ContentType

def check_user_able_to_see_page(*groups):
    #print('groupssss',groups)
    def decorator(function):
        #print('-----fucnc name--------',function.__name__)
        def wrapper(request, *args, **kwargs):
            #print(f'{groups}',request, args,kwargs)
            if request.user.groups.filter(name__in=groups).exists() | request.user.is_superuser:
                return function(request, *args, **kwargs)
            #raise Http404
            raise PermissionDenied
        return wrapper

    return decorator


def CheckUserPermission(group):
    #content_type = ContentType.objects.get_for_model(profileReadeMore)
    #print('content_type',content_type)
    #permission = Permission.objects.filter(content_type=content_type)
    #print('permission',permission)        
    #print('Group',  Group.objects.first().permissions.all())
    #print('Group',Group.objects.filter(name__in=['mirones','admin']))
    permissions=[]
    for x in Group.objects.get(name=group).permissions.all():
        app=ContentType.objects.get(id=x.content_type_id)
        #print(f'{app.app_label}.{x.codename}')
        permissions.append(f'{app.app_label}.{x.codename}')
    return permissions  
