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

Django trabalha com 'Migrations'
- O que são 'Migrations'?
- As migrações (Migrations) são uma forma de atualizar o esquema do banco de dados para acompanhar as mudanças em seus modelos (models). Quando você define modelos em um aplicativo Django, as migrações são usadas para criar, modificar ou excluir tabelas, colunas e restrições no banco de dados subjacente de acordo com as alterações feitas nos modelos.
- Rollback de Migrações: Além de aplicar migrações, você também pode reverter migrações anteriores para desfazer as alterações no esquema do banco de dados.
- As migrações em Django são gerenciadas usando o comando manage.py migrate. Quando você executa este comando, o Django verifica as migrações pendentes e aplica as alterações necessárias no banco de dados.
- As migrações no Django são uma parte essencial do ciclo de vida do desenvolvimento de aplicativos, permitindo que você mantenha o esquema do banco de dados sincronizado com a estrutura dos modelos de forma controlada e automatizada.
- É possível visualizar o diretorio de migrations dentro do app.

Como criar as 'Migrations'?
- Execute o comando: ```python manage.py makemigrations```

Como executar a atualização de banco com 'Migrations'?
- Execute o comando: ```python manage.py migrate```

Django Super User
- Para ter acesso a pagina '/admin', é necessário executar 'Migrations' antes.
- Após execução das 'Migrations' é possível acessar a página de super usuario, mas para logar é necessário criar um super usuario.
- Para criar um super usuario execute o comando: ```python manage.py createsuperuser```
- Em project > settings.py é possível visualizar as validações para a criação de senha do super user. Procure por AUTH_PASSWORD_VALIDATORS.
- Para realizar a troca de senha, execute: ```python manage.py changepassword <NOME_DE_USUARIO>```
- Exemplo: ```python manage.py changepassword john```