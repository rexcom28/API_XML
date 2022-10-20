
from django.shortcuts import render
from django.views import View
from . forms import ProfileForm,UserForm
from . models import Profile, Technology_type

from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin



class ProfileView(LoginRequiredMixin, View):
    form_class      = UserForm
    model           = User    
    template_name   = 'Profiles/myProfile.html'
    

    def get(self, request, *args, **kwargs):
        instance_           = User.objects.get(username=request.user)  
        instance_profile    = Profile.objects.get(user=request.user)
        form                = self.form_class(instance=instance_)
        form_profile        = ProfileForm(instance=instance_profile)       
 
        return render(request, self.template_name, {
            'form': form, 
            'form_profile':form_profile,
            'img':instance_profile.avatar
        })
    
    def post(self, request, *args, **kwargs):
        instance_           = User.objects.get(username=request.user)
        instance_profile    = Profile.objects.get(user=request.user)
        form                = self.form_class(request.POST, request.FILES, instance=instance_)
        form_profile        = ProfileForm(request.POST, request.FILES,instance=instance_profile)

        if form.is_valid():            
            form.save()
            if form_profile.is_valid():
                img =form_profile.instance.avatar                
                form_profile.save()
        
        return render(request, self.template_name, {
            'form':form, 
            'form_profile':form_profile,
            'img':img
        })



def frontpage(request, username=None):
     
    profile = User.objects.get(username=username).profile    
    profileReadMore = profile.profileRM.all()
    profileGoodAt = profile.profileRM.all().filter(section_type='GoodAt')

    profile_work_images = profile.profile_works.all()
    techs = profile_work_images.values('data_type').distinct()
    socials = profile.profile_social.all()    
    
    
    return render(request, 'Profiles/frontpage.html' ,{
        'profile':profile,
        'profileReadMore': profileReadMore,
        'profileGoodAt':profileGoodAt,
        'profile_work_images':profile_work_images,
        'techs':techs,
        'socials':socials
    })

def index(request):
    profiles = Profile.objects.all()    
    return render(request, 'Profiles/index.html', {
        'profiles':profiles
    })