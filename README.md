# projeto_imobiliaria
Projeto relativo à conclusão da trilha de Python da Enforce no programa Campinas Tech Talents

Para executar esse projeto, é necessário ter o Python, o NodeJS e PostgreSQL instalados

### Inicializar o servidor

1. Entrar na pasta API

2. Ativar o ambiente virtual

`.\Scripts\activate`

3. Instalar as bibliotecas necessárias e dependências

`pip install -r requirements.txt`

4. Entrar na pasta projeto

6. Para criar as tabelas no banco de dados, em outro terminal, dentro da pasta projeto e com o ambiente env ativado, digite:

>python
>from api import db
>db.create_all()

5. Para inicializar o servidor, na linha de comando:

>set FLASK_APP=api.py
>flask run

### Inicializar o Front-end

1. Entrar na pasta Front-end

2. Na primeira vez que for executar o código na máquina, no terminal, digite para instalar as dependências:

`npm install`

3. Após a instalação das depenências do projeto, ainda no terminal, digite:

`ng serve --open`
