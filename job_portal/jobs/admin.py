from msilib import CreateRecord
from django.contrib import admin

# from job_portal.candidates.models import Candidate
from.models import job
from candidates.models import CandidateJobMap

class CanditateInline(admin.TabularInline): 
    model = CandidateJobMap

    def get_readonly_fields(self,request,*args, **kwargs):
      if request.user.is_superuser:
            return []
      else:
            return ('candidate',)  

class JobAdmin(admin.ModelAdmin):
    
    exclude = ('create',)
    list_display = ('position_name','create',)
    inlines = (CanditateInline,) 
    
    def get_queryset(self, request, *args, **kwargs):
      if request.user.is_superuser:
            return job.objects.all()
      else:
            return job.objects.filter(create=request.user)  
    
    
    def get_list_display(self, request,*args, **kwargs):
        if request.user.is_superuser:
            return('position_name','create',)
        else:
            return('position_name',)
    
    
    def save_model(self, request, obj, form,  change):
        if not obj.pk: 
            #assign the creater only  on creation and updation
         obj.create = request.user
         obj.save()
     

admin.site.register(job,JobAdmin)