Instale o Django com o seguinte comando:
- ```pip install django```

Crie o projeto Django executando o seguinte comando:
- ```django-admin startproject project .```

Busque por Django .gitignore no google e adicione no arquivo .gitignore os arquivos que devem ser ignorados.

Execute o projeto executando o seguinte comando:
- ```python manage.py runserver```

Crie o app contact
- ```python manage.py startapp contact```

Adicione o app criado contact a lista INSTALLED_APPS

Sempre que criar um novo app, adicione-o a lista INSTALLED_APPS

Adicione o diretorio base_templates a lista de TEMPLATES/DIRS em project/settings.py
- base_static
- base_templates

Adicione o diretorio base_static a project/settings.py
- Adicione uma nova lista nomeada STATICFILES_DIRS
- Coloque na lista o diretorio base_static

As pastas criadas dentro dos apps com nome templates são automaticamente reconhecidas pelo Django.

