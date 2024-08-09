## Hello World Django

Este projeto é destinado ao aprendizado da linguagem python e do framework Django com base na formação da Alura [Django: crie aplicações em Python](https://cursos.alura.com.br/formacao-django)

# Para rodar o projeto no windows:

- Crie a venv rodando:
    ```
    python -m virtualenv .venv
    ```

- Ative a virtualenv criada:
    ```
    .venv\Scripts\activate
    ```

- Instale as dependências do projeto:
    ```
    pip install -r .\requirements.txt
    ```

- Colete os arquivos estáticos para utilização do Django:
    ```
    python manage.py collectstatic
    ```

- Rode as migrations:
    ```
    python manage.py migrate
    ```

- Inicie o servidor:
    ```
    python manage.py runserver
    ```

# Dicas para o processo de desenvolvimento:

- Quando criar um novo model:
    - Lembre-se :
        > *Todo modelo é uma classe Python, subclasse de django.db.models.Model.*
    
    - Lembre-se de gerar seu arquivo de migration:
        ```
        python manage.py makemigrations
        ```

- Quando criar um novo arquivo html:
    - Lembre-se de carregar os arquivos estáticos no início do arquivo:
        ```
        {% load static %}
        ```

    - Caso seja um arquivo de conteúdo, ou seja, que deva herdar cabeçalho e rodapé, por exemplo, não se esqueça de adicionar os arquivos herdados, carregar os arquivos estáticos e de referenciá-lo como bloco de conteúdo:
        ```
        {% extends 'app/base.html' %}
        {% load  static%}
        {% block content %}
            # código html aqui
        {% endblock %}
        ```

    - Caso seja necessário isolar algum código para reaproveitá-lo em várias telas (ideia de componentes), crie os arquivos no diretório 'template/app/partials' e inicie seu nome com underline ( _ )

        **(exemplo)**
        ```
        <projeto>/templates/<app>/partials/_footer.html
        ```

- Boas práticas:
    - Manter o arquivo 'requeriments.txt' sempre atualizado (para garantir o funcionamento do projeto, pois é o arquivo de referência para a instalação das dependências necessárias):
        ```
        pip freeze > requirements.txt
        ```

    - No arquivo setup/settings.py, ao referenciar os apps, utilizar sua classe de configuração ao invés de apenas o seu nome, para garantir a importação de todas configurações atribuídas ao app

        Para isso, na lista INSTALLED_APPS, adicione a classe do app criada no arquivo apps.py

        **(exemplo)**
        ```
        INSTALLED_APPS = [
            'galery.apps.GaleryConfig',
        ]
        ```

    - Nos templates, usar blocos de conteúdo para evitar a repetição de código e facilitar manutentação
        ```
        <body>
            {% include 'galery/partials/_header.html' %}
            {% block content %}{% endblock %}
            {% include 'galery/partials/_footer.html' %}
        </body>
        ```


- Inserir dados no banco utilizando terminal python / django:
    - Entre no python shell:
        ```
        python manage.py shell
        ```

    - Importe o modelo (exemplo):
        ```
        from galery.models import Photo
        ```

    - Crie o objeto desejado (exemplo):
        ```
        photo = Photo(title="Nebulosa de Carina", subtitle="webbtelescope.org | NASA | James Webb", description="webbtelescope.org | NASA | James Webb teste teste teste webbtelescope.org | NASA | James Webb", image="carina-nebula.png")
        ```

    - Salve o objeto criado:
        ```
        photo.save()
        ```

    - Para visualizar a saída da função __str__ do objeto criado:
        ```
        photo.objects.all()
        ```