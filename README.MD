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






[1] Built-in Filters (Template Tags) - https://docs.djangoproject.com/pt-br/4.0/ref/templates/builtins/#built-in-filter-reference