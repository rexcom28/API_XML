
from django.shortcuts import render, redirect
from django.views import View
from . forms import ProfileForm,UserForm, CustomContactForm
from . models import Profile, Technology_type
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
class ProfileView(LoginRequiredMixin, View):
    form_class      = UserForm
    model           = User    
    template_name   = 'Profiles/myProfile.html'
    
 
    def get(self, request,*args, **kwargs):
        
        instance_           = User.objects.get(username=request.user)  
        instance_profile    = Profile.objects.get(user=request.user)
        form                = self.form_class(instance=instance_)
        form_profile        = ProfileForm(instance=instance_profile)       
 
        return render(request, self.template_name, {
            'form': form, 
            'form_profile':form_profile,
            'img':instance_profile.avatar,
            'username':instance_.username
        })
    
    def post(self, request,*args, **kwargs):
        instance_           = User.objects.get(username=request.user)
        instance_profile    = Profile.objects.get(user=request.user)
        form                = self.form_class(request.POST, request.FILES, instance=instance_)
        form_profile        = ProfileForm(request.POST, request.FILES,instance=instance_profile)
        img =form_profile.instance.avatar
        
        if form.is_valid():            
            form.save()
            
            if form_profile.is_valid():
                
                form_profile.save()
                messages.add_message(request, messages.INFO, 'Profile info saved!')

        return render(request, self.template_name, {
            'form':form, 
            'form_profile':form_profile,
            'img':img,
            'username':instance_.username
        })


@login_required(login_url='login2')
def frontpage(request, username=None):
     
    profile = User.objects.get(username=username).profile    
    profileReadMore = profile.profileRM.all()
    profileGoodAt = profile.profileRM.all().filter(section_type='GoodAt')

    profile_work_images = profile.profile_works.all()
    techs = profile_work_images.values('data_type').distinct()
    socials = profile.profile_social.all()    
    contactForm = CustomContactForm(initial={'contact_to_user':request.user})
    if request.method== 'POST':
        
        contactForm = CustomContactForm(request.POST)         
        if contactForm.is_valid():
            contactForm.save()
            messages.add_message(request, messages.INFO, 'Message sent successfully!')
            return redirect('frontpage', username=username)
    return render(request, 'Profiles/frontpage.html' ,{
        'profile':profile,
        'profileReadMore': profileReadMore,
        'profileGoodAt':profileGoodAt,
        'profile_work_images':profile_work_images,
        'techs':techs,
        'socials':socials,
        'contactForm':contactForm,
        
    })

@login_required(login_url='login2')
def index(request):
    profiles = Profile.objects.all()    
    return render(request, 'Profiles/index.html', {
        'profiles':profiles
    })