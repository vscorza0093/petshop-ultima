# Petshop Ultima School

Esse Readme contém anotações e explicações sobre o projeto de finalização de curso de Desenvolvimento Python da Ultima School.

Neste projeto estamos utilizando:

1. HTML, CSS, Bootstrap
2. Python
3. Django
4. Rest Framework



### Tag <form>

A tag <form> é usada para criar um formulário HTML para input do usuário

A tag <form> pode conter um ou mais dos seguintes elementos:

* <input>
* <textarea>
* <button>
* <select>
* <option>
* <optgroup>
* <fieldset>
* <label>
* <output>

A tag <form> possui diversos atributos, como autocomplete, ou especificações de codificação de caracteres, nome, validação, relação entre formulário e documento.

Um atributo muito importante é o _method_ que servirá para especificar o método HTTP que será utilizado ao enviar os dados do formulário.
Estão disponíveis os métodos *GET* e *POST*

Dentro do `bootstrap` temos diversas classes de formulários que podem ser utilizadas, dependendo das necessidades da nossa aplicação.
As mais comuns são `form-select` e `form-control`.

Podemos ver toda a ação de um botão `submit` em um formulário `post` através do Inspetor do Navegador, na aba `Network`.
A partir do momento que submetemos nosso formulário, o método `POST` será chamado e todas as informações preenchidas no nosso formulário serão transmitidas para o servidor e todas as informações contidas no formulário serão exibidas através da aba `Payload` do Inspetor.


