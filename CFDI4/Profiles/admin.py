from atexit import register
import site
from django.contrib import admin
from .models import Profile, profileReadeMore, profile_work_images, Technology_type, profilie_social_media


class profileReadMoreAdmin(admin.ModelAdmin):
    list_display=['profile', 'title', 'description', 'section_type']


class profile_work_imagesAdmin(admin.ModelAdmin):
    list_display= ['profile', 'image', 'title', 'caption', 'data_type', 'desc' ]

admin.site.register(Technology_type)
admin.site.register(Profile)
admin.site.register(profileReadeMore, profileReadMoreAdmin)
admin.site.register(profile_work_images, profile_work_imagesAdmin)
admin.site.register(profilie_social_media)
