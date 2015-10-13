from django.contrib import admin
from .models import Sala, Ficha


class SalaAdmin(admin.ModelAdmin):
    '''
        Admin View for Sala
    '''
    list_display = ('nome', 'turno')
    #list_filter = ('',)
    #raw_id_fields = ('',)
    #readonly_fields = ('',)

admin.site.register(Sala, SalaAdmin)


class FichaAdmin(admin.ModelAdmin):
    '''
        Admin View for Ficha
    '''
    list_display = ('n_ficha', 'crianca', 'responsavel', 'telefone', 'sala',
                    'ativo')
    list_filter = ('sala',)
    search_fields = ['n_ficha', 'crianca', 'responsavel']


admin.site.register(Ficha, FichaAdmin)
