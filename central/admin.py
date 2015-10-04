from django.contrib import admin
from .models import Sala, Ficha


class SalaAdmin(admin.ModelAdmin):
    '''
        Admin View for Sala
    '''
    pass
    #list_display = ('',)
    #list_filter = ('',)
    #raw_id_fields = ('',)
    #readonly_fields = ('',)
    #search_fields = ['']

admin.site.register(Sala, SalaAdmin)


class FichaAdmin(admin.ModelAdmin):
    '''
        Admin View for Ficha
    '''
    pass
    #list_display = ('',)
    #list_filter = ('',)
    #raw_id_fields = ('',)
    #readonly_fields = ('',)
    #search_fields = ['']

admin.site.register(Ficha, FichaAdmin)
