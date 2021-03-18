# PROJETO IMOBILIÁRIA

Projeto relativo à conclusão da trilha de Python da Enforce no programa Campinas Tech Talents

Foram usados, neste projeto:
##### Front-end:
* [Angular](https://angular.io/)

##### Back-end:
* [Postgres](https://www.postgresql.org/)
* [SQLAlchemy](https://www.sqlalchemy.org/)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)


Para executar esse projeto, é necessário ter o Python, o NodeJS e PostgreSQL instalados.

### Inicializar o servidor

0. No PostgreSQL, criar o database Imobliaria usando o script `createDatabase.sql` presente na pasta Banco de dados;

1. Entrar na pasta API: `cd API`

2. Para ativar o ambiente virtual, no terminal, digite: `.\Scripts\activate`

3. Instalar as bibliotecas necessárias e dependências, no terminal, digite: `pip install -r requirements.txt`

4. Entrar na pasta projeto: `cd projeto`

5. Para criar as tabelas no banco de dados, em outro terminal, dentro da pasta projeto e com o ambiente env ativado, digite:

>python  
>from api import db  
>db.create_all()  

6. É preciso executar o script para popular as tabelas de domínio. O script `InsertTabelasDominio.sql` está na pasta Banco_de_dados deste projeto.

7. Para inicializar o servidor, na linha de comando:

>set FLASK_APP=api.py  
>flask run  

### Inicializar o Front-end

1. Entrar na pasta Front-end

2. Na primeira vez que for executar o código na máquina, no terminal, digite para instalar as dependências: `npm install`

3. Após a instalação das dependências do projeto, ainda no terminal, digite: `ng serve --open`
