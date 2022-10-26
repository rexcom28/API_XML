from contactforms.models import Contact
from django.db import models
from django.contrib.auth.models import User

def user_avatar_directory_path(instance, filename):
    return 'avatars/{0}/{1}'.format(instance.user.username, filename)



class Profile(models.Model):

    user = models.OneToOneField( User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    #avatar = models.ImageField(default='avatar.png', upload_to='avatars')
    avatar = models.ImageField(default='avatar.png', upload_to=user_avatar_directory_path)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    follows = models.ManyToManyField('self', related_name='followed_by',symmetrical=False, blank=True, null=True)
    job_title = models.CharField(max_length=55, blank=True, null=True)
    good_at_bio = models.TextField(blank=True)
    mywork_bio = models.TextField(blank=True)
    contact_msn = models.TextField(blank=True)

    #show sections
    show_socials = models.BooleanField(default=True)
    show_ReadMore = models.BooleanField(default=True)
    show_GoodAt = models.BooleanField(default=True)
    show_WorkImages = models.BooleanField(default=True)

    def __str__(self):
        return str(self.user)

class profilie_social_media(models.Model):
    TW='Twitter'
    FB='Facebook'
    IN='Linkedin'
    socials = (
        (TW,'Twitter'),
        (FB,'Facebook'),
        (IN,'Linkedin'),
    )
    profile     = models.ForeignKey(Profile, related_name='profile_social', on_delete=models.CASCADE)
    social_type = models.CharField(max_length=30, choices = socials)
    url         = models.URLField(max_length=255, blank=True, null=True)
class profileReadeMore(models.Model):
    ReadMore    = 'ReadMore'
    GoodAt      = 'GoodAt'
    left        = 'left'
    right       = 'right'
    types_sec = (
        (ReadMore,'Read More'),
        (GoodAt,'Good At'),
    )
    le_ri = (
        (right, 'image to right'),
        (left, 'image to left'),
    )
    profile = models.ForeignKey(Profile, related_name='profileRM', on_delete=models.CASCADE)
    title   = models.CharField(max_length=55)
    description = models.TextField()
    section_type= models.CharField(max_length=10, choices=types_sec, default='ReadMore')
    left_rigth  = models.CharField(max_length=5,choices=le_ri, default='left')
    image = models.ImageField(blank=True, null=True)

class Technology_type(models.Model):
    tech = models.CharField(max_length=55, unique=True)
    desc = models.CharField(max_length=150)


class profile_work_images(models.Model):

    # def c_tech():
    #     return [(tech.tech, f'{tech.tech}-{tech.desc}') for tech in Technology_type.objects.all()]

    profile = models.ForeignKey(Profile, related_name='profile_works', on_delete=models.CASCADE)
    image   = models.ImageField()
    title   = models.CharField(max_length=25)
    caption = models.CharField(max_length=25)
    data_type = models.CharField(max_length=30)#, choices =c_tech())
    desc    = models.CharField(max_length=65, blank=True)


class CustomContact(models.Model):

    contact_to_user  = models.ForeignKey(Profile, related_name='profile_contactuser', on_delete=models.CASCADE)
    name = models.CharField(max_length=120,blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    subject = models.CharField(max_length=200)
    message = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.contact_to_user.user.username