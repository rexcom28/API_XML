from django.shortcuts import render
from django.contrib.auth.models import Group,Permission
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView,UpdateView
from django.views.generic import ListView
from .forms_admin import GroupForm

class Group_List_View(LoginRequiredMixin,ListView):
    paginate_by = 10
    model = Group
    template_name = 'Config/Groups/ListView.html'
    login_url='login2'

class Group_Add_View(LoginRequiredMixin, CreateView):
    model=Group
    form_class= GroupForm
    template_name='Config/Groups/edit_Group.html'
    success_url='/list_group'
    login_url='login2'
    def get_context_data(self, **kwargs):
        context = super(Group_Add_View, self).get_context_data(**kwargs)
        context['qs']= self.kwargs['group']        
        return context

    def get(self, request, *args, **kwargs):
        self.object = None
        qs=Permission.objects.all().filter(content_type__app_label=kwargs['group'])    
        form = GroupForm(qs=qs)
        context = self.get_context_data(object=self.object,form=form)
        return self.render_to_response(context)
    
    def post(self, request, *args, **kwargs):        
        self.object =None
        qs=Permission.objects.all().filter(content_type__app_label=kwargs['group'])
        form= GroupForm(request.POST,qs=qs)
        if form.is_valid():            
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

class Group_Edit_View(LoginRequiredMixin, UpdateView):
    model=Group
    form_class= GroupForm
    template_name='Config/Groups/edit_Group.html'
    success_url='/list_group'
    login_url='login2'
    
    def get(self, request, *args, **kwargs):
        self.object = Group.objects.get(pk=kwargs['pk'])        
        App= self.object.permissions.all().values('content_type__app_label').first()        
        App= App['content_type__app_label']
        qs=Permission.objects.all().filter(content_type__app_label=App)
        form = GroupForm(instance=self.object, qs=qs)
        context = self.get_context_data(
            object=self.object,
            qs=App,
            form=form
        )
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        App= self.object.permissions.all().values('content_type__app_label').first()
        App= App['content_type__app_label']
        qs=Permission.objects.all().filter(content_type__app_label=App)
        form = GroupForm(request.POST, instance=self.object, qs=qs)
        if form.is_valid():            
            return self.form_valid(form)
        else:
            return self.form_invalid(form)