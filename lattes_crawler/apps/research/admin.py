from django.contrib     import admin
from ..research.models  import Research

    
class ResearchAdmin(admin.ModelAdmin):
    '''
    '''
    list_display = ('id', 'lattes_id', 'lattes_information', )

admin.site.register(Research, ResearchAdmin)