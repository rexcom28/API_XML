from .models import Profile
from Config.models import CSSConf
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def post_save_create_profile(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        CSSConf.objects.create(user=instance)
        
        
@receiver(post_save, sender=User)
def save_profile(sender,instance,created, **kwargs):
    instance.profile.save()    
    if not created:        
        instance.user_confCSS.get_or_create(user=instance)
