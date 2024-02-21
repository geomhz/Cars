# Sistema de Gerenciamento de Pedidos - Prime Telefonia

## Sobre o Projeto

Este projeto é um simples sistema de cadastro de carros desenvolvido com o framework Django. Ele é projetado para facilitar a organização de cadastro de carros, oferecendo diversas funcionalidades úteis para uma gestão eficiente.

### Funcionalidades

- **Tela de Login:** Autenticação segura para acessar o sistema.
- **Tela de registro** Cadastro de usuários para acessar o sistema.
- **Filtro para pesquisa de carros** O filtro facilita a pesquisa de carro por nome/marca.
- **Create/Read/Update/Delete (CRUD) carros** Para quem está logado é possível adicionar um novo cadastro, ver lista de carros cadastrados, atualizar o cadastro do carro já existente, ou deletar algum carro existente. (CRUD)
- **Administrador (DJANGO-ADMIN):** Controle e administração de todos os acessos presentes na plataforma.

## Iniciando

Essas instruções vão te ajudar a ter uma cópia do projeto funcionando na sua máquina local para desenvolvimento e teste.

### Pré-requisitos

Instale os seguintes pré-requisitos para rodar o projeto:

- Python 3.8+ instalado na máquina.

### Instalação

Siga os passos abaixo para configurar o ambiente de desenvolvimento:

1. Clone o repositório
```bash
git clone https://github.com/geomhz/car-store-django.git

```

1. Crie um ambiente virtual e ative
```bash
Windows: python -m venv venv
         venv/scripts/activate

Linux/Mac: python3 -m venv venv
           source venv/bin/activate
```

3. Instale as dependências
```bash
pip install -r requirements.txt
```
4. Execute as migrações
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Inicie o servidor
```bash
python manage.py runserver
```

### Dependências

Lista de dependências do projeto:
```bash
asgiref==3.7.2
Django==5.0.2
pillow==10.2.0
sqlparse==0.4.4
tzdata==2024.1
```

## Uso

Ao iniciar o sistema com o comando:
```bash
python manage.py runserver
```

Abra um navegador e navegue localmente:
```bash
http://127.0.0.1:8000/
```

Visualize a lista de carros disponíveis sem ter acesso á edições:
OBS: Ao clicar em cima de alguma imagem de carro da lista disponível você terá acesso aos detalhes do carro.
```bash
http://127.0.0.1:8000/cars/
```

Cadastre-se no sistema para conseguir ter acesso ao CRUD (CREATE, READ, UPDATE E DELETE):
```bash
http://127.0.0.1:8000/register/
```

Faça login para conseguir acessar o sistema:
```bash
http://127.0.0.1:8000/login/
```

Após o login com a nova conta criada você terá acesso á edições do carro ao clicar na imagem de algum carro.
```bash
http://127.0.0.1:8000/cars/
```

Registre um novo carro. As imagens de upload serão adicionadas automaticamente á pasta "media" localizada na raiz do projeto!
```bash
http://127.0.0.1:8000/new_car/
```

Pronto! Agora que sabe navegar no sistema já pode explorar!!

## Contato
Meu nome é Geovanne Murata!

Website - [Acesse meu website!](https://geomurata.com/)

Linked In - [Acesse meu LinkedIn!](https://www.linkedin.com/in/geovanne-murata/)

WhatsApp - [Me envie uma mensagem no WhatsApp!](https://api.whatsapp.com/send/?phone=5511952842140)

Link do Projeto: [car-store-django](https://github.com/geomhz/car-store-django/)