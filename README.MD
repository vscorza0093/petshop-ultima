# Petshop Ultima School

Esse Readme contém anotações e explicações sobre o projeto de finalização de curso de Desenvolvimento Python da Ultima School.

O projeto final será um sistema para pet shop. Este sistema deverá ter a funcionalidade de agendar banho para um dia específico respeitando o a quantidade máxima de agendamentos por dia.

Descrição dos recursos:

```
Crie uma categoria de animais para que o pet shop saiba qual animal pode tomar banho no local;
Crie uma página de agendamento na qual os usuários possam agendar banho para seus animais selecionando uma data disponível, uma categoria de animal e alguns dados pessoais como nome e telefone para entrar em contato caso algo mude ou para quando o banho no animal for finalizado;
Os gerentes de pet shop desejam uma página onde possam verificar os agendamentos. Esta página pode ser uma página do administrador ou outra página fora do administrador (como um painel);
Na API deve haver uma forma de recuperar uma categoria de animal com uma lista dos animais que tomaram banho no mês anterior;
A API também deve permitir a criação de uma nova reserva.
```



### Tag <form>

A tag <form> é usada para criar um formulário HTML para input do usuário

A tag <form> pode conter um ou mais dos seguintes elementos:
```
* <input>
* <textarea>
* <button>
* <select>
* <option>
* <optgroup>
* <fieldset>
* <label>
* <output>
```
A tag <form> possui diversos atributos, como autocomplete, ou especificações de codificação de caracteres, nome, validação, relação entre formulário e documento.

Um atributo muito importante é o _method_ que servirá para especificar o método HTTP que será utilizado ao enviar os dados do formulário.
Estão disponíveis os métodos *GET* e *POST*

Dentro do `bootstrap` temos diversas classes de formulários que podem ser utilizadas, dependendo das necessidades da nossa aplicação.
As mais comuns são `form-select` e `form-control`.

Podemos ver toda a ação de um botão `submit` em um formulário `post` através do Inspetor do Navegador, na aba `Network`.
A partir do momento que submetemos nosso formulário, o método `POST` será chamado e todas as informações preenchidas no nosso formulário serão transmitidas para o servidor e todas as informações contidas no formulário serão exibidas através da aba `Payload` do Inspetor.


### Sistema de Templates

Antes de entender o funcionamento de uma submissão de formulário, devemos entender qual a utilidade de um sistema de Templates. Até agora criamos páginas "estáticas", isto é, o conteúdo html dela é fixo, nada é alterado de acordo com algo que venha do banco de dados ou algum cálculo feito no nosso código Python.

Entretanto, a ideia de usar um sistema de templates é justamente fazer com que a página enviada para o usuário seja dinâmica, ou seja, ela deve ser alterada de acordo com:
```
* Algo que esteja salvo no banco de dados - EX: (Abas do menu principal)
* Usuário que esteja acessando a página - EX: (Exibir nome do usuário logado)
* Algum cálculo feito no código - EX: (Cálculo de juros de acordo com inputs do usuário)
```

Para realizar tais ações iremos utilizar:

```
* Variáveis: valores que ficarão disponíveis para serem exibidos no html, acessíveis através de um nome (na prática é um dicionário Python)
* Template Tags: marcações especiais que realizarão ações na página e irão ajudar a controlar o fluxo das variáveis (representam comandos como IF e For)
* Filtros: alteram o conteúdo de exibição de uma variável e fazem com que o conteúdo de uma variável seja exibido de uma forma diferente - EX: (o filtro upper vai fazer com que os caracteres de um texto fiquem em caixa alta)

```Python
def contato(request):
    context = {
        'telefone': '(99) 99999-9999',
        'responsavel': 'Maria da Silva',
    }
    return render(request, "contato.html", context)
```

No código acima criamos um dicionário com duas chaves `telefone` e `responsavel`

E colocamos este dicionário como o 3º parâmetro da função render. Desta forma indicamos ao Django que teremos disponíveis no template essas duas variáveis (telefone e responsavel).

Neste código, colocamos um texto indicando que é possível entrar em contato através do formulário ou ligando para um determinado número. Entretanto, em vez de escrever o número, colocamos a marcação: {{ telefone }}.

Esta marcação, com duas chaves abrindo e duas chaves fechando, indica ao Django que queremos exibir o valor de uma variável, — no caso, a variável de nome telefone. 

Desta forma conseguimos criar páginas dinâmicas, pois essas variáveis podem agora vir de uma consulta do banco de dados, de um cálculo matemático ou simplesmente de uma informação do usuário logado. 

Além das variáveis, ainda temos os filtros e as templatetags. Um exemplo de uso do filtro é:

```html
  <h1>Fale Conosco</h1>
  <p> 
    Envie uma mensagem através do formulário abaixo ou ligue para o telefone {{ telefone }}. Falar com a responsável {{ responsavel }}
  </p>
```
Na modificação acima, colocamos o |upper após o nome da variável responsavel. É assim que o filtro funciona: você coloca o “|” e em seguida o filtro desejado, e este filtro faz com que todos os caracteres da variável fiquem em caixa alta.

Para consultar todos os filtros disponíveis no sistema de templates do Django, basta consultar a documentação oficial de `Built-in Filters`[1].

Isto ocorreu porque o Django tem alguns mecanismos de segurança, seno que um deles é para um tipo de ataque chamado cross site request forgery ou apenas CSRF. Para entender melhor como funciona este tipo de ataque, é interessante ler o artigo neste link.


### Submetendo formulário

Nossa página de contato já tem um formulário, agora falta fazermos a lógica de submeter este formulário. Na tag form é possível perceber que existe o atributo action=””. Ele indica, ao submetê-lo, a página para a qual os dados serão enviados e a página atual (o vazio representa a página atual). Além deste atributo vamos usar também o atributo method=”post”, que por sua vez indica que o método HTTP utilizado será o POST. No geral, utiliza-se POST para quando você está enviando dados que se imagina que serão salvos ou processados de forma mais complexa; e GET quando é um formulário de busca.

Isto ocorreu porque o Django tem alguns mecanismos de segurança, sendo que um deles é para um tipo de ataque chamado cross site request forgery ou apenas CSRF.

Para se proteger desse tipo de ataque, o Django indica o uso de uma templatetag chamada {% csrf_token %}. Ela vai criar um campo escondido neste formulário e, quando enviado, o Django vai pegar este campo e processar para saber se aquela submissão de formulário é realmente de um usuário válido que carregou a página anteriormente.


### Django Form

Podemos resgatar os dados enviados pelo usuário na submissão de um formulário. Assim, podemos simplesmente pegar cada valor no request.POST e realizar alguma ação lógica como enviar um e-mail ou salvar no banco de dados.

Entretanto, em vez de começar a pegar esses dados pelo request.POST, vamos utilizar uma ferramenta que vem com o Django: o Forms. O Django Forms é uma parte do framework que faz validações de dados enviados por formulários, e é muito útil na validação de dados, e também na geração do HTML dos campos, além de converter os valores textuais vindos do formulários em objetos Python. Um exemplo de conversão: ao digitarmos uma data no formato dd/mm/aaaa, o Forms recebe esse texto, verifica se é uma data válida (se esse dia existe no calendário) e em seguida retorna um objeto Python do tipo “date”, isto é, uma data formal em Python.

O sistema de Forms é composto da seguinte forma:

```
* Classe Form: representa todo o formulário que será processado, e é nela que definimos quais campos teremos e algumas regras de validações gerais;
* Field: é um campo específico do formulário que indica quais validações devem ser feitas, e de que tipo;
* Widget: é a forma como um Field será representado no HTML, isto é, como um campo vai gerar o HTML (se vai ser um input text, textarea, select etc.).
Bibliografia
```

Então, para usar o Django Forms nesta página de contato, vamos precisar criar um arquivo chamado forms.py na mesma pasta onde está o views.py, com o seguinte conteúdo:

```Python
from django import forms


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
```

A classe ContactForm vai herdar dados de uma classe chamada forms.Form, e com isso ela vai ganhar algumas características do sistema de Forms. Em seguida, vamos declarar quais os campos esse formulário terá:

```
nome: vai ser do tipo CharField, que corresponde a um campo de texto simples no formulário e irá se transformar num input text.

email: vai ser do tipo EmailField, que corresponde a um campo de texto que valida se valor informado se parece com um email, e no html vai se transformar num input email

menssage: vai ser do tipo CharField também, porém, como queremos que seja um campo de texto maior (textarea), precisaremos indicar o widget desse campo.
```

Com nossa classe criada e seus campos definidos, vamos testá-la primeiramente no terminal do Django (terminal do Python com o ambiente Django carregado). Para isso, vamos parar o comando runserver e rodar o seguinte comando: `python manage.py shell`

Agora estamos no terminal do Python, mas com o ambiente Django carregado, pois assim conseguimos trabalhar melhor. Vamos importar a nossa classe criada e então criar um dicionário simulando o que seriam os dados enviados do formulário e por fim vamos criar nosso form.


Quando chamamos o form.is_valid(), estamos verificando se todos os campos são válidos. Neste caso, ele retornou True, pois todos os campos foram preenchidos e o campo email realmente tinha um e-mail válido. Em seguida usamos o as_p() para gerar o HTML desse formulário em forma de tags p.

Na prática, o form vai pegar cada campo, colocar uma tag p e em seguida gerar o HTML do label e do input. É possível verificar que foram criados os tipos corretos nos campos nome e email, e o campo mensagem virou um textarea, pois tínhamos mencionado que o widget dele seria justamente um textarea. Além disso, os campos estão preenchidos com os valores informados no dicionário dados.

No exemplo acima, o campo email não tem um e-mail válido e o campo mensagem está vazio, portanto, é possível verificar que foi criada uma tag ul que contém uma outra tag li, e ela contém uma mensagem de erro já traduzida (afinal, no começo do projeto indicamos o idioma pt-BR).

Tanto essa mensagem como a forma como os campos vão ser disponibilizados são passíveis de customizações, afinal, este HTML acima não é compatível com o Bootstrap  (em cada campo falta a class=”form-control”, além de outros detalhes).

Assim, para facilitar nosso trabalho, vamos utilizar uma biblioteca chamada: django-bootstrap-v5. Para instalá-la basta rodar no terminal: `pip install django-bootstrap-v5`

```python
from baseapp.forms import ContactForm

def contato(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
    context = {
        'telefone': '(99) 99999-9999',
        'responsavel': 'Maria da Silva',
        'form': form
    }
    return render(request, "contato.html", context)
```

No código acima, verificamos se o método acessado é o GET (criamos o form vazio) ou o POST (criamos o form com os dados do request.POST). Por fim, precisamos colocar este form no contexto para que fique disponível no template.

Vamos agora alterar o contato.html para gerar esse form. Primeiro vamos adicionar uma templatetag no início dele:
```
{% load bootstrap5 %}
```

Assim como em Python, o sistema de templates do Django também tem templatetags e filtros nativos, isto é, não é necessário importá-los. Além disso, é possível criar novos templatetags e filtros (como é o caso deste App django bootstrap v5) e carregá-los com a opção load. Com a biblioteca boostrap5 carregada, agora temos acesso a algumas templatetags extras. Vamos usar uma delas para renderizar o form no formato que o Bootstrap precisa:

```
<main>
  <h1>Fale Conosco</h1>
  <p> 
    Envie uma mensagem através do formulário abaixo ou ligue para o telefone {{ telefone }}. Falar com a responsável {{ responsavel|upper }}
  </p>
  <form action="" method="post">
    {% csrf_token %}
    {% bootstrap_form form %}

    <hr>
    <button type="submit" class="btn btn-primary">Enviar Mensagem</button>
  </form>
</main>
```

No trecho acima, substituímos a escrita manual dos campos do formulário pela chamada da nova templatetag bootstrap_form. Templatetags podem receber parâmetros como se fossem funções Python, assim, esta recebe o form, que é a variável que foi definida no contexto no arquivo views.py e é um ContatoForm. 

Nosso formulário mudou um pouco, já que agora todos os campos estão alinhados verticalmente, mas é possível ajustar essa posição caso necessário.  De toda forma, o HTML foi gerado conforme indicado pelo Bootstrap, sem a necessidade de escrever um código longo. Agora, vamos  submeter a página para verificar se as mensagens de erro são exibidas.

Quando utilizarmos o método POST, o código entrará no else e executará se o form estiver válido (tudo preenchido corretamente). Vamos colocar a variável sucesso como True, e ela será adicionada no contexto também. Agora vamos alterar o contato.html para que, caso essa variável sucesso seja True, uma mensagem de sucesso seja exibida:

```
  {% if success %}
  <p class="alert alert-success">Mensagem enviada com sucesso!</p>
  {% endif %}
```

No código acima vemos mais uma templatetag, o IF. Ela tem o mesmo comportamento de um IF em Python: será repassada uma condição, e caso seja confirmada, o HTML entre o {% if sucesso %} e o  {% endif %} será colocado na página que será acessada pelo usuário. É como se fosse um print da página: se confirmada pelo IF, a tag p com class=”alert alert-success” será exibida. A página será carregada normalmente ao ser acessada pela primeira vez, e após o preenchimento correto dos dados, a mensagem de sucesso aparecerá.

Assim, no trecho de código do views.py onde colocamos sucesso = True, poderíamos fazer alguma outra lógica como salvar os dados no banco ou enviar um e-mail.


### ORM (Object-relational Mapper) e Migrate

ORM no Django Model é uma abstração que permite que classes Python representem tabelas no banco de dados. Estas classes devem ser escritas no arquivo `models.py` de cada módulo. Sabemos que alguns módulos já estão na configuração `INSTALLED_APPS` do arquivo `settings.py`, ou seja, já tem suas tabelas para serem criadas. Então vem a pergunta: como fazer o django criar essas tabelas e como indicar que vamos utilizar o sqlite3?

Isso se responde na variável DATABASES, do mesmo arquivo `settings.py`.

Na configuração padrão, está indicado que iremos utilizar o sqlite3 e o nome do arquivo do nosso banco de dados será: `db.sqlite3`.

Nem todo módulo precisa ter modelos (tabelas), mas é comum tê-los. Por isso, para que o Django crie as possíveis tabelas das aplicações, precisamos rodar um novo comando, conhecido como `migrate`.

Utilizaremos o comando da seguinte forma `python .\manage.py migrate`. E após a conclusão da execução, um novo diretório, chamado `migrations` será criado no nosso módulo.

O Django Models, além de permitir que uma classe Python vire uma tabela e que manipulações sejam realizadas nos dados sem usar SQL diretamente, também permite que se faça um versionamento do banco de dados através de migrações (migrations).

As migrações são atualizações na estrutura do banco de dados. Imagine que criamos uma funcionalidade que exigia ter uma tabela com cinco campos, e alguns meses depois, percebemos que seria útil ter um novo campo. Com isso, precisariamos fazer uma atualização na tabela. No sistema de migrações do Django, podemos fazer a alteração na classe Python que representa a tabela, adicionando o campo extra, em seguida rodamos alguns comandos para gerar automaticamente um código Python que irá adicionar esse campo na tabela.

Com o DBeaver poderemos visualizar as tabelas que foram criadas em nosso banco de dados. 

As tabelas que começam com o prefixo `auth` são as tabelas do sistema de usuários que já vem com o Django.

Sobre as outras tabelas:

```
* django_admin_log: controla as atividades dos usuários no sistema administrativo do Django
* django_content_type: armazena informações sobre todas as tabelas e classes Python (models) da aplicação
* django_migrations: armazena as migrações que foram efetivamente executadas no banco de dados. Se algum colega de projeto gerar novas migrações (criar ou modificar tabelas), ao rodar o `migrate`o Django irá pegar apenas as migrações ainda não executadas
* django_session: controla a sessão de usuários (armazena dados gerais sobre o acesso dos usuários)
```

Para criar nossas próprias tabelas, precisamos, primeiro, identificar o que faz sentido ser armazenado no banco de dados. No nosso projeto temos uma página de contato que não realiza nenhuma ação quando um usuário envia uma mensagem. Vamos corrigir isto, inserindo um novo código dentro do arquivo `models.py`, que está dentro da nossa pasta `baseapp`

```python
from django.db import models

class Contact(models.Model):
  name = models.CharField(max_length=50)
  email = models.EmailField(max_length=75)
  date = models.DateTimeField(auto_now_add=True)
  message = models.TextField()

```

No código acima, criamos uma classe chamada Contact que herda de uma outra classe `models.Model`. Assim como quando foi criado um form, nós indicamos quais os campos que queremos, a diferença aqui é que esses campos irão se transformar em colunas no nosso banco de dados.

Com nossa classe criada, agora precisamos criar uma migração, que é um arquivo Python que irá indicar o que vai ser criado no banco de dados. Felizmente esse arquivo é gerado de forma automática, executando o seguinte comando: `python .\manage.py makemigrations`

O comando `makemigrations` é responsável por verificar se o banco de dados está compatível com nosos modelos, ou seja, identificar se os nossos modelos (classes que herdam de models.Model) estão com os mesmos campos e opções correspondentes ao banco de dados atual. Caso haja alguma diferença (novas classes/modelos, novos campos ou alterações nos campos), esse comando vai identificá-la e criar um arquivo Python com uma rotina que faz a alteração no banco de dados: create table, alter table, drop column, entre outros comandos.

Um novo arquivo foi criado, e neste arquivo é indicada uma migração de criação de modelo, que na prática vai criar a tabela indicada. Agora iremos rodar o comando que efetiva as migrações, o `migrate`. Ele identifica quais migrações ainda não foram executadas: `python .\manage.py migrate`

```
Operations to perform:
  Apply all migrations: admin, auth, baseapp, contenttypes, sessions
Running migrations:
  Applying baseapp.0001_initial... OK
```

Agora podemos visualizar, dentro do DBeaver, a nova tabela criada.

É possível perceber que o nome da tabela ficou baseapp_contact. Esse é o padrão do Django, usar o nome do módulo com o nome do modelo. Entretanto, existe uma coluna chamada `id` que não foi declarada na hora que criamos nosso modelo, uma vez que o Django exige uma coluna que seja a chave primária da tabela. Com isso, se não for definida uma coluna para a chave primária, o Django cria automaticamente esse campo `id`.


### Operações de Persistência

Para testarmos o nosso modelo criado anteriormente, vamos executar o comando shell do Django, que faz com que um terminal do Python abra com o ambiente Django disponível: `python .\manage.py shell`

A partir deste comando, abrimos o ambiente de shell do Django, onde poderemos criar uma instância de qualquer modelo que criamos anteriormente no arquivo `models.py` e salvá-la no banco de dados.

```python

In[1]: from base.models import Contact
In[2]: contact = Contact()
In[3]: contact.name = "Vinicius"
In[4]: contact.email = "vinicius@email.com"
In[5]: contact.message = "Mensagem de teste"
In[6]: contact.save()

```

No código acima importamos a classe contato e criamos uma instância (um registro do banco de dados ainda não salvo). Após utilizarmos a função `save()` que está definida na classe `Model` que está sendo herdada pela nossa classe Contact, os dados inseridos na instância criada são persistidos no banco de dados. A função save é responsável por gerar o comando `Insert` correspondente a este registro e, assim, efetivar o salvamento da informação no banco de dados. 

Enquanto não finalizarmos a sessão do Shell Django, poderemos fazer alterações nos dados inseridos no banco de dados, utilizando a instância criada anteriormente. O ORM do Django é inteligente para perceber que estamos querendo atualizar informações e no momento em que utilizarmos a função `save()`, o Django não irá mais realizar um `Insert` no banco de dados, mas sim um `Update`, atualizando nosso registro salvo anteriormente. 

Uma outra forma de salvar um dado usando nossos modelos é através de uma função chamada `create`, presente no atributo `objects` da classe Model, herdada pelas nossas classes modelos.

```python

In[1]: from base.models import Contact
In[2]: contact = Contact.objects.create(name="Vinicius", email="vinicius@email.com", message="Mensagem de teste")

```

Utilizando a função `create()` da propriedade objects, uma nova informação será sempre salva, um novo id será criado no banco de dados. Essa é a principal diferença de `create()` para `save()`.

Além de salvar informações, o ORM do Django permite consultar dados. Para isso devemos utilizar a função Get da propriedade `objects`.

```python

In[1]: from base.models import Contact
In[2]: contact1 = Contact.objects.get(id=1)
In[3]: contact1.name
'Vinicius'
In[4]: contact1.email
'vinicius@email.com'

```

Essa função Get recebe o nome do campo na tabela e o valor que se deseja consultar. Na prática, um comando SQL `Select` será gerado para fazer a consulta no banco de dados. No entanto, a função irá se limitar a retornar apenas um registro, e assim os filtros utilizados devem garantir que apenas uma informação seja retornada. Caso desejemos consultar todos os dados de determinada tabela, devemos seguir da seguinte forma:

```python

In[1]: from base.models import Contact
In[2]: contacts = Contact.objects.all()
In[3]: for contact in contacts:
          print(f"Name:{contact.name}\nMessage:{contact.message}")

'Name:Vinicius'
'Message:Nothing to say'
'Name:Stella'
'Message:Somos o Petshop mais fofo do mundo'

```

A função `all()` faz uma consulta para retornar todos os dados da tabela e é possível fazer um loop for em cima do resultado para manipular todas as informações vindas do banco de dados. Desta forma, podemos navegar sobre os registros retornados e, por exemplo, imprimir o nome e email.

É possível criar quaisquer consultas no banco de dados utilizando o ORM do Django, sem precisar escrever o código SQL correspondente.



## Modelform

Agora que já sabemos como funciona um modelo do Django, vamos fazer com que nosso formulário de contato salve efetivamente a mensaegm de contato no banco de dados. Para isso, vamos ajustar o arquivo `views.py`




































[1] Built-in Filters (Template Tags) - https://docs.djangoproject.com/pt-br/4.0/ref/templates/builtins/#built-in-filter-reference