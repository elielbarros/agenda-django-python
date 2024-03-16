from django.urls import path
from contact import views

# Crie um namespace para evitar problemas com outros app's que tambem
# utilizam a palavra chave index como url. Essa configuração é
# automaticamente definida pelo django.
app_name = 'contact'

urlpatterns = [
    path('', views.index, name='index'),
]
