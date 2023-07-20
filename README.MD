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


