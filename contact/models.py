from django.db import models
from django.utils import timezone

# Create your models here.
# id (primary key) - automaticamente criado pelo django
# first_name (string, last_name (string), phone (string)
# email (email), created_date (date), description (text)
# category (foreign key), show (boolean), owner (foreign key)
# picture (imagem)

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        # Se nao estiver configurado no admin o list_display, aparecerá como
        # está aqui
        return f'{self.name}'

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    # blank=True, significa que esse campo não necessita ser preenchido
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    # Utilizando o timezone.now, significa que o usuario nao pode atualizar
    # essa informação.
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    # VAI CRIAR AS SUBPASTAS media/pictures/ano/mes/arquivo.extensao
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 blank=True, null=True)
    
    def __str__(self) -> str:
        # Se nao estiver configurado no admin o list_display, aparecerá como
        # está aqui
        return f'{self.first_name} {self.last_name}'
