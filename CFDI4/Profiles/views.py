from django.db.models import Q
from CFDI4.GroupValidator import check_user_able_to_see_page, sameUserMixin
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import DeleteView, CreateView
from django.views.generic import ListView
from . forms import (
    ProfileForm,UserForm, 
    CustomContactForm, ProfileReadMoreForm,
    ProfileReadMore_AddForm, CustomContactForm_isRead,
    TechsTypesForm_ADD,
    TechsTypesForm,
    SocialsForm,
    Work_Images_Form,
)
from . models import (
    Profile, 
    Technology_type, 
    profileReadeMore, 
    CustomContact,
    profilie_social_media,
    profile_work_images,
)
from django.contrib.auth.models import User
from django.contrib.auth.mixins import PermissionRequiredMixin,LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import Group,User
from django.contrib.contenttypes.models import ContentType
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.http import Http404


class ProfileView(LoginRequiredMixin, View):
    form_class      = UserForm
    model           = User
    template_name   = 'Profiles/myProfile.html'
    login_url = 'login2'
    
    

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
class ProfileReadMoreEditView(LoginRequiredMixin, View):
    form_class = ProfileReadMoreForm
    @method_decorator(sameUserMixin('Profiles','profileReadeMore'))    
    def get(self, request, *args, **kwargs):    
        if request.is_ajax and request.headers.get('X-Requested-With') == 'XMLHttpRequest':            
            oid = request.GET.get('oid', '')
            try:            
                readMore = profileReadeMore.objects.values().get(id=oid)
                return JsonResponse({'readMore':readMore}, status=200)
            except:
                readMore = {'error':'No encontrado'}            
                return JsonResponse(readMore, status=404)
        else: # cancel the GET method call none ajax            
            raise Http404("None Ajax call")
    
    def post(self, request, *args, **kwargs):
        if request.POST['id']!='':
            rm = profileReadeMore.objects.get(id=request.POST['id'])
            form = self.form_class(request.POST, request.FILES, instance=rm)
        else:
            form = ProfileReadMore_AddForm(request.POST, request.FILES)
            form.instance.profile_id=request.user.id
        
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Section updated successfully!')
        else:
            messages.add_message(request, messages.ERROR, f'{form.errors}')
        return redirect('readmore_view')
        
class ProfileReadMore_Delete_View(LoginRequiredMixin, DeleteView):
    model = profileReadeMore
    success_url='/readMore/'

#@method_decorator(check_user_able_to_see_page('mirones'),name='dispatch')
class ProfileReadMoreListView(
    #PermissionRequiredMixin,
    LoginRequiredMixin, ListView):

    # def CheckUserPermission(group):
    #     permissions=[]
    #     for x in Group.objects.get(name=group).permissions.all():
    #         app=ContentType.objects.get(id=x.content_type_id)
    #         permissions.append(f'{app.app_label}.{x.codename}')
    #     return permissions
    
    # permission_required = (CheckUserPermission('admin'))
    
    paginate_by = 10
    model = profileReadeMore
    template_name= 'Profiles/prof_ReadMore.html'
    login_url = 'login2'
    def get_context_data(self, **kwargs):
        context = super(ProfileReadMoreListView, self).get_context_data(**kwargs)
        #adding form to the context listview for edit in modal in ProfileReadMoreEditView call
        context['form']= ProfileReadMoreForm()
        return context

    def get_queryset(self,*args, **kwargs):
        
        search      =self.request.GET.get('search', '')
        description =self.request.GET.get('description',False)
        title       =self.request.GET.get('title',False)
        #print(search, description, title)
        
        qs = super(ProfileReadMoreListView, self).get_queryset(*args, **kwargs)
        if 'username' in self.kwargs:           
            qs =qs.filter(profile__user__username=self.kwargs['username'])
        else:                       
            qs = qs.filter(profile=self.request.user.profile)

        if search or (description or title):
            qs = qs.filter(Q(description__icontains=search)|Q(title__icontains=search))
        if title and not description:
            qs = qs.filter(Q(title__icontains=search))
        if not title and description:
            qs = qs.filter(Q(description__icontains=search))
        
        return qs

class Contact_is_readed_view(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        ins = CustomContact.objects.get(id=request.POST['id'])
        form = CustomContactForm_isRead(request.POST, instance=ins)        
        if form.is_valid():
            form.instance.is_readed=True
            form.contact_to_user_id=request.user.id
            form.save()
            messages.add_message(request, messages.INFO, 'message  readed!')
        else:
            messages.add_message(request, messages.ERROR, f'{form.errors}')

        return redirect('contact_list_view')

class Contact_ListView(LoginRequiredMixin, ListView):
    paginate_by = 10
    model = CustomContact
    template_name = 'Profiles/Contacts/contact_list.html'
    login_url='login2'
    def get_context_data(self,**kwargs):
        context = super(Contact_ListView, self).get_context_data(**kwargs)
        context['form']= CustomContactForm_isRead()
        return context
    def get_queryset(self,*args, **kwargs):
        search      =self.request.GET.get('search', '')
        name        =self.request.GET.get('name', False)
        email       =self.request.GET.get('email', False)
        print(search,name,email)
        qs = super(Contact_ListView, self).get_queryset(*args, **kwargs)
        qs = qs.filter(contact_to_user_id=self.request.user.id) 

        if search or (name or email) :
            qs = qs.filter(Q(name__icontains=search)|Q(email__icontains=search))
        if name and not email:
            qs = qs.filter(Q(name__icontains=search))
        if not name and email:
            qs = qs.filter(Q(name__icontains=search))
        
        return qs

class Techs_ListView(LoginRequiredMixin, ListView):
    paginate_by =10
    model = Technology_type
    template_name: str = 'Profiles/Techs/tech_list.html'
    login_url= 'login2'
    def get_context_data(self, **kwargs):
        context = super(Techs_ListView, self).get_context_data(**kwargs)
        context['form'] = TechsTypesForm()
        return context

    def get_queryset(self,*args, **kwargs):
        search = self.request.GET.get('search','')
        tech = self.request.GET.get('tech','')
        desc = self.request.GET.get('desc',False)
        
        qs = super(Techs_ListView, self).get_queryset(*args, **kwargs)
        if search or (tech or desc):            
            qs = qs.filter(
            Q(tech__icontains=search)|
            Q(desc__icontains=search))
        if search and tech and not desc:
            qs = qs.filter(tech__icontains=search)
        if search and not tech and desc:
            qs = qs.filter(desc__icontains=search)
        return qs 

class Techs_Delete_View(LoginRequiredMixin, DeleteView):
    model = Technology_type
    success_url='/techs/'
class Techs_Edit_View(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):          
        if request.is_ajax and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            oid = request.GET.get('oid', '')            
            try:
                techs = Technology_type.objects.values().get(id=int(oid))
                return JsonResponse(techs, status=200)
            except:
                techs = {'error':'No encontrado'}
                return JsonResponse(techs, status=404)
        else:
            raise Http404("None Ajax call")    
    def post(self, request, *args, **kwargs):
        is_added = True if request.POST['id']!='' else False
        is_added_STR = 'Updated' if request.POST['id']!='' else 'Added'
        if is_added:
            instance_ = Technology_type.objects.get(id=int(request.POST['id']))
            form = TechsTypesForm(request.POST, instance=instance_)
        else:            
            form = TechsTypesForm_ADD(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO,
            f'Tech {is_added_STR} successfully!')
        else:
            messages.add_message(request, messages.ERROR, f'{form.errors}')
        return redirect('techs_view')

class Socials_Delete_View(LoginRequiredMixin, DeleteView):
    model = profilie_social_media
    success_url='/socials/'
class Socials_ListView(LoginRequiredMixin, ListView):
    paginate_by =10
    model = profilie_social_media
    template_name: str = 'Profiles/Socials/social_list.html'
    login_url= 'login2'
    def get_context_data(self, **kwargs):
        context = super(Socials_ListView, self).get_context_data(**kwargs)
        context['form'] = SocialsForm()
        return context

    def get_queryset(self,*args, **kwargs):
        search = self.request.GET.get('search','')
        social = self.request.GET.get('social','')
        url = self.request.GET.get('url','')


        qs = super(Socials_ListView, self).get_queryset(*args, **kwargs)
        qs = qs.filter(profile=self.request.user.profile)
        if search or (social or url):
            qs =qs.filter(
                Q(social_type__icontains=search) |
                Q(url__icontains=search)
            )
        if search and social and not url:
            qs = qs.filter(Q(social_type__icontains=search))
        if search and not social and url:
            qs = qs.filter(Q(url__icontains=search))
        return qs
    
class Socials_Edit_View(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        if request.is_ajax and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            oid = request.GET.get('oid', '')
            
            try:
                socials= profilie_social_media.objects.values().get(id=int(oid))            
                return JsonResponse(socials, status=200)
            except:
                raise JsonResponse({'error':'No encontrado'}, status=404)
        else:
            return Http404("None Ajax call")
    def post(self, request, *args, **kwargs):
        is_new = (False,'Updated') if request.POST['id'] != '' else (True, 'Added')
        if is_new[0]==True:
            form = SocialsForm(request.POST)
            form.instance.profile= request.user.profile
        else:
            instance_ = profilie_social_media.objects.get(id=request.POST['id'])            
            form =SocialsForm(request.POST, instance=instance_)
        if form.is_valid():
            
            form.save()
            messages.add_message(request, messages.INFO,
            f'Social {is_new[1]} successfully!')
        else:
            messages.add_message(request, messages.ERROR, 
            f'{form.errors}')
        return redirect('socials_view')

class Work_Images_Delete_View(LoginRequiredMixin, DeleteView):
    model = profile_work_images
    success_url= '/workimages/'

class Work_Images_List_View(LoginRequiredMixin, ListView):
    paginate_by=10
    model = profile_work_images
    template_name = 'Profiles/WorkImages/workImages_list.html'
    login_url='login2'
    def get_context_data(self, **kwargs):
        context = super(Work_Images_List_View, self).get_context_data(**kwargs)
        context['form'] = Work_Images_Form()
        return context
    
    def get_queryset(self,*args, **kwargs):
        
        search      =self.request.GET.get('search', '')
        description =self.request.GET.get('description',False)
        title       =self.request.GET.get('title',False)
        #print(search, description, title)
        
        qs = super(Work_Images_List_View, self).get_queryset(*args, **kwargs)
        if 'username' in self.kwargs:           
            qs =qs.filter(profile__user__username=self.kwargs['username'])
        else:                       
            qs = qs.filter(profile=self.request.user.profile)

        if search or (description or title):
            qs = qs.filter(Q(desc__icontains=search)|Q(title__icontains=search))
        if title and not description:
            qs = qs.filter(Q(title__icontains=search))
        if not title and description:
            qs = qs.filter(Q(desc__icontains=search))
        
        return qs

class work_Images_Edit_View(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        if request.is_ajax and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            oid = request.GET.get('oid', '')
            
            try:
                workimgs= profile_work_images.objects.values().get(id=int(oid))            
                return JsonResponse(workimgs, status=200)
            except:
                raise JsonResponse({'error':'No encontrado'}, status=404)
        else:
            return Http404("None Ajax call")

    def post(self, request, *args, **kwargs):
        is_new = (False,'Updated') if request.POST['id'] != '' else (True, 'Added')
        if is_new[0]==True:
            form = Work_Images_Form(request.POST,request.FILES)
            form.instance.profile= request.user.profile
        else:
            instance_ = profile_work_images.objects.get(id=request.POST['id'])
            form =Work_Images_Form(request.POST, request.FILES, instance=instance_)
        

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO,
            f'Work Images {is_new[1]} successfully!')
        else:
            messages.add_message(request, messages.ERROR, 
            f'{form.errors}')
        return redirect('workimages_view')


"""----------------------Functions base views"""


@login_required(login_url='login2')
def frontpage(request, username=None):
    profile = User.objects.get(username=username).profile    
    profileReadMore = profile.profileRM.all()
    profileGoodAt = profile.profileRM.all().filter(section_type='GoodAt')

    profile_work_images = profile.profile_works.all()
    techs = profile_work_images.values('data_type').distinct()
    socials = profile.profile_social.all()    
    contactForm = CustomContactForm(initial={
        'contact_to_user':profile,
        'email':request.user.email,
        'name':request.user.get_full_name,
    })
    if request.method== 'POST':
        print(request.POST)
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

