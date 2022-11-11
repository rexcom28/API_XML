import imp
from django import forms
from django.contrib import admin
from django.contrib.contenttypes.models import ContentType

from django.contrib.auth.models import Permission

admin.site.register(Permission)
admin.site.register(ContentType)

from .models import (Profile, profileReadeMore, profile_work_images,
  Technology_type,
  profilie_social_media, CustomContact)


class TechnologyAdmin(admin.ModelAdmin):
    list_display= ['id','tech']

class profileSocialAdmin(admin.ModelAdmin):
    list_display=['profile','social_type', 'url']

class profileReadMoreAdmin(admin.ModelAdmin):
    list_display=['profile', 'title', 'description', 'section_type']


class profile_work_imagesAdmin(admin.ModelAdmin):
    list_display= ['profile', 'image', 'title', 'caption', 'data_type', 'desc' ]


class ProfileForm(forms.ModelForm):
    class Meta:
        model =Profile
        exclude = ['user', 'follows']
class profileAdmin(admin.ModelAdmin):
    form= ProfileForm

admin.site.register(CustomContact)
admin.site.register(Technology_type, TechnologyAdmin)
admin.site.register(Profile, profileAdmin)
admin.site.register(profileReadeMore, profileReadMoreAdmin)
admin.site.register(profile_work_images, profile_work_imagesAdmin)
admin.site.register(profilie_social_media, profileSocialAdmin)
