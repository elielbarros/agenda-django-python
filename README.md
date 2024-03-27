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
- eliel, senha de sempre

Django Database Connection
- O django usa, por padrao, o sqlite como banco de dados.
- Ao executar as 'Migrations', o framework cria e atualiza todas as tabelas que a aplicação tem mapeado.
- É interessante ler as documentações a seguir:
  - https://docs.djangoproject.com/pt-br/4.2/topics/db/models/
  - https://docs.djangoproject.com/pt-br/4.2/ref/models/fields/#field-choices

Onde criar Models?
- Para criar um Model, é necessário acessar o app desejado e o arquivo models.py
- Usar o arquivo models.py para criar a classe que representa o modelo desejado, seguindo o padrao do Django

Como fazer a migração dos Models para o banco de dados?
- Executar a atualização de banco com 'Migrations'
- Execute primeiramente o comando: ```python manage.py makemigrations```
- É possível visualizar o resultado do comando dentro da pasta do app no diretorio 'migrations'
- Execute em seguida o comando: ```python manage.py migrate```
- É possível visualizar o resultado do comando acima, com o dbeaver. A tabela criada terá o nome do app + o nome da classe

Como alterar time zone da aplicação?
- Acesse o arquivo settings.py e atualize a constante TIME_ZONE para o tipo que desejar
- Valor padrao é TIME_ZONE = 'UTC'
- Exemplo: TIME_ZONE = 'America/Sao_Paulo'

Como alterar o idioma do Django?
- Acesse o arquivo settings.py e atualize a constante LANGUAGE_CODE para a linguagem desejada
- Valor padrao é LANGUAGE_CODE = 'en-us'
- Exemplo: LANGUAGE_CODE = 'pt-br'

Como usar django shell para executar CRUD de um modelo?
- Executar o comando: ```python manage.py shell```
- Insert ![insert_contact_django_shell.png](.estudo_static%2Finsert_contact_django_shell.png)
- Insert sem save ![create_contact_django_shell.png](.estudo_static%2Fcreate_contact_django_shell.png)
- Select com condição ![select_all_with_condition_contact_django_shell.png](.estudo_static%2Fselect_all_with_condition_contact_django_shell.png)
- Select com ordenação '-id' (menos) descrescente ![select_order_by_contact_django_shell.png](.estudo_static%2Fselect_order_by_contact_django_shell.png)