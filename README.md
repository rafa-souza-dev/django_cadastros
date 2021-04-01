# Introdução:

Sistema de cadastro criado em Django, onde é possível cadastrar dados pessoais num banco de dados Sqlite3, edita-los e excluí-los.
O site possui apenas um APP, chamado de cadastro.

O framework que utilizei para construção dos templates e organização foi o Fomantic-UI.

Decidi por não criar um arquivo ".gitignore", para que se tenha uma vizualização completa do projeto.

Para o acesso da aba admin/, o superuser criado tem senha=admin e login=admin

# Templates:

Dentro do APP cadastro, entrando na pasta de templates, encontra-se 6 templates(HTML) diferentes. Sendo eles base, home, lista, pessoa, tabela e deletar.

- Home: Nesse template há o menu horizontal e um menu lateral, ambos importados por uma função "extends" do arquivo "base.html" e load static. Fora isso, há também o formulário de cadastro do site. No formulário existem os inputs obrigatórios(Nome, Sobrenome, Idade, Data de Nascimento e E-mail) e os inputs não obrigatórios(Apelido e Observação). As abas de nome e sobrenome são preenchidas automaticamente, onde é feita uma requisição de uma API do tipo REST: https://gerador-nomes.herokuapp.com/nome/aleatorio; O formulário foi criado com base na tabela Pessoa(models.Model) que encontra-se no arquivo de "models.py". Para organização do formulário e importação de dados, utilizei a biblioteca "crispy-forms", instalada facilmente via terminal pelo código pip install django-crispy-forms. No arquivo settings.py, é preciso implementar na lisa de APP's, um APP com nome de 'crispy_forms'. Além disso, criar uma variável CRISPY_TEMPLATE_PACK = 'bootstrap4', dessa forma todo formulário do crispy será baseado no modelo do bootstrap4. Lembrando de importar a CDN do mesmo;
- Lista: Assim como na Home, na lista de edição é importado a "base.html" via extends. Essa lista dá acesso a todas as pessoas cadastradas no sistema, com um botão para pesquisa que filtra o primeiro nome. É possível, nessa tela, editar ou excluir um cadastro do banco de dados, tendo 2 botões pra cada pessoa;
- Tabela: A tela de Tabela, mostra ao usuário uma tabela com todas as pessoas cadastradas, sendo seus dados obrigatórios(Nome, Sobrenome, Idade, Data de Nascimento e E-mail) juntamente com o ID de cada registro;
- Pessoa: O template de "pessoa.html" é, basicamente, a tela de edição de um registro. Ao entrar numa url referente a pessoa/pessoa<int:pk>, todos os inputs são automaticamente preenchidos, possibilitando a edição de cada um;
- Deletar: "deletar.html" é uma tela para excluir um registro. A tela será aberta via url deletar/pessoa<int:pk>, onde irá pedir a confirmação para deletar o registro.

# Acrécimos:

- Decidi, por uma questão de melhor organização, que o site tivesse três telas principais(Cadastro, Tabela, Lista de Edição) ao invés de duas. Dessa forma é possível pesquisar o nome da pessoa desejada na tela de Lista, e resolver se quer edita-la ou excluí-la. As três telas podem ser acessadas facilmente pelo menu horizontal, fixado em todos os templates do site.

# Dificuldades:

- Na questão de gerar nomes aleatórios pela API, criei um arquivo chamado "requisicao.py". Nele existem duas funções, uma com a biblioteca requests e outra com a biblioteca json. Dessa forma, consegui fazer a requisição e gerar um nome e sobrenome aleatórios, mas o não consegui fazer com que o nome mudasse sempre que a home fosse aberta ou atualizada, infelizmente. Tentei de várias maneiras, utilizando funções e condicionais, mas nada deu certo. Por fim, os nomes são gerados e preenchem os campos, mas não mudam quando a página é atualizada.
- Na parte de validação de dados, não consegui criar uma forma de a idade se relacionar com a data de nascimento, dessa forma é possível que uma pessoa se cadastre com uma idade totalmente desconexa de uma data_nascimento.

# Sites que me ajudaram:

https://django-crispy-forms.readthedocs.io/en/latest/install.html#installing-django-crispy-forms

https://fomantic-ui.com/

https://getbootstrap.com/docs/5.0/getting-started/introduction/

https://favicon.io/

https://fontawesome.com/
