## Hello World Django

Este projeto é destinado ao aprendizado da linguagem python e do framework Django com base na formação da Alura [Django: crie aplicações em Python](https://cursos.alura.com.br/formacao-django)

# Para rodar o projeto no windows:

- Crie a venv rodando o seguinte comando:
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

- Inicie o servidor:
```
python manage.py runserver
```