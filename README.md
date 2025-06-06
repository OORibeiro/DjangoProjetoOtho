# FatecTech
#Português

Projeto de estudo com sistema de vendas, banco de dados e produtos exibidos via uma fake API.  
Sistema web de e-commerce para venda de produtos, desenvolvido com Django.

---

## Requisitos

- Python 3.x (usado: `3.12.10`)  
- Django 5.x (usado: `5.2.1`)  
- Bibliotecas adicionais:
  - matplotlib==3.10.3
  - pillow==11.2.1
  - requests==2.32.3
- Outras dependências estão no arquivo `requirements.txt`

---

## Instalação e Execução

1. **Clone o repositório**:

```bash
git clone https://github.com/OORibeiro/DjangoProjetoOtho

2. Entre na pasta do projeto:


cd DjangoProjeto

3. Crie e ative um ambiente virtual(desinstale a atual antes):

python -m venv venv

4. Instale as dependências:

pip install -r requirements.txt

5.Rode as migrações do banco:

 python manage.py migrate

6. (Opcional) Crie um superusuário para acessar o admin:

python manage.py createsuperuser

7.Inicie o servidor de desenvolvimento:

python manage.py runserver

8. Acesse o sistema no navegador:

http://127.0.0.1:8000/

obs:

Caso queira ter acesso de adm para excluir outros usuários vá nas linhas 61, 93, e mude o e-mail dessas linhas e cadastre um usuário com esse novo e-mail.


#Ingles

Study project featuring a sales system, database, and products displayed through a fake API.  
Web-based e-commerce system for selling products, developed with Django.

---

## Requirements

- Python 3.x (used: `3.12.10`)  
- Django 5.x (used: `5.2.1`)  
- Additional libraries:
  - matplotlib==3.10.3
  - pillow==11.2.1
  - requests==2.32.3
- Other dependencies are listed in the `requirements.txt` file


1. **Clone the repository**:

```bash
git clone https://github.com/OORibeiro/DjangoProjetoOtho

2. Enter the project folder:

cd DjangoProjeto

3. Create and activate a virtual environment (uninstall the current one first):

python -m venv venv

4. Install the dependencies:

pip install -r requirements.txt

5. Run the database migrations:

 python manage.py migrate

6. (Optional) Create a superuser to access the admin:

python manage.py createsuperuser

7. Start the development server:

python manage.py runserver

8. Access the system in the browser:

http://127.0.0.1:8000/

Note:

If you want to have admin access to delete other users, go to lines 61, 93, and change the email on these lines and register a user with this new email.

