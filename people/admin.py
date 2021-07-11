from django.contrib import admin
from .models import Person

admin.site.site_header = "Casa Danielle"
admin.site.site_title = "Casa Danielle"
admin.site.index_title = "Bem vindo!"


class PersonAdmin(admin.ModelAdmin):
  list_display = ('name', 'created_at')
  list_filter = ['gender', 'state']
  search_fields = ['name']
  fieldsets = [('Identificação', {
      'fields':
      ['name', 'mother_name', 'born_date', 'cpf', ('rg', 'rg_ssp'), 'gender']
  }),
               ('Endereço', {
                   'fields': [
                       'address_line_1', 'address_line_2', 'neighbourhood',
                       'state', 'city', 'postal_code', 'residence_type'
                   ]
               }),
               ('Contato', {
                   'fields': [
                       'email', ('ddd_private_phone', 'private_phone'),
                       ('ddd_message_phone', 'message_phone')
                   ]
               }),
               ('Outras informações', {
                   'fields': ['observation'],
                   'classes': ('collapse', ),
               })]


# Register your models here.
admin.site.register(Person, PersonAdmin)
