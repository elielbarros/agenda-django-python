from django.contrib import admin
from contact import models
# Register your models here.
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    # Permite a ordenação pelos campos que foram colocados em list_display
    list_display = ('id', 'first_name', 'last_name', 'phone',)
    # Permite uma ordenação especifica
    # Para ordenar pelo id de forma decrescente coloque '-id'
    ordering = ('-id',)
    # Permite a cricação de um filtro pelo campo 'created_date'
    # list_filter = ('created_date',)
    # Permite a pesquisa pelos campos inseridos na tupla
    search_fields = ('id', 'first_name', 'last_name')
    # Permite a paginação por pagina
    list_per_page = 10
    # Permite a visualização maxima de 200 contatos
    list_max_show_all = 200
    # Permite que os campos da tupla sejam editados na tela principal
    list_editable = ('first_name', 'last_name')
    # Permite configurar o link de acesso aos detalhes do contato
    # Se o link estiver na lista list_ediitable, ocorre um erro, nao pode
    # estar nos dois
    list_display_links = ('id', 'phone')
    