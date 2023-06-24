# Antes de usar o sheettoform_1.py

* Certifique-se de instalar o python3 na versão mais atual.
* Caso você utilize python em outros projetos no seu computador, é recomendável que você crie um ambiente virtual para as bibliotecas usadas neste projeto.

## Criando e utilizando um ambiente virtual

1. Para criar um ambiente virtual, instale o **virtualenv** usando o pip mesmo:
    ```
    $ pip install virtualenv
    ```
2. Crie um ambiente virtual dentro do repositório deste código:
    ```
    $ virtualenv .venv
    
    ou,

    $ python -m virtualenv .venv
    ```
3. Toda vez que for usar o script **execute este passo** para entrar no ambiente virtual:
    ```
    windows powershell:
    > .venv\Scripts\activate

    linux terminal:
    $ source .venv/bin/activate
    ```

## Instale as bibliotecas necessárias

Para instalar as bibliotecas necessárias, utilize o comando abaixo. Certifique-se de que, caso use um ambiente virtual, você tenha executado o [passo 3](#criando-e-utilizando-um-ambiente-virtual) da seção anterior. Para saber se está no ambiente virtual procure pela string "(.venv)" logo no início da linha de comando no seu terminal.

```
pip install -r requirements.txt
```

# Usando sheettoform_1.py

Modifique as informações necessárias no script no escopo do comentário "INPUT".

* **FORM_URL** corresponde à URL completa de submissão dos dados contidos em um elemento form. Basicamente a url descrita no atributo "action" do elemento. Essa URL irá receber um _FormData object_ usando o método post.
    ```python
    FORM_URL = 'http://127.0.0.1:5000/form/submit'
    ```
* **SHEET_ID** corresponde ao ID do arquivo de planilhas que contém a planilha que será mapeada para o formulário. Dá para obter esta ID observando o link de compartilhamento do arquivo de planilhas no google. Sendo o link como abaixo:
    ```
    https://docs.google.com/spreadsheets/d/1EKXkCrWfV8avj_3mOInwqUvNC_a5P1b3J6d6HhcswwQ/edit?usp=sharing
    ```
    O valor de **SHEET_ID** será tal que:
    ```python
    SHEET_ID = '1EKXkCrWfV8avj_3mOInwqUvNC_a5P1b3J6d6HhcswwQ'
    ```

* **SHEET_NAME** corresponde ao nome da planilha, i.e. a aba no arquivo de planilhas onde estão os dados que serão mapeados para o formulário. Neste caso a planilha "Dados" será utilizada:
    ```python
    SHEET_NAME = 'Dados'
    ```

* **SHEET_FIELDMAP** é um dicionário python em que a chave corresponde à coluna na planilha e o valor ao nome do campo de formulário.
    ```python
    SHEET_FIELDMAP = {
        'Nome': 'name', 
        'Sobrenome': 'lastname', 
        'Telefone': 'phone', 
        'Empresa': 'company'
    }
    ```

Após estas mudanças para adequação ao seu propósito, você pode executar o script diretamente:

```
$ python ./sheettoform_1.py
```

# Testando em um servidor local

Para testar a efetividade do script, rode uma aplicação servidora localizada no diretório **form_site_example**. Para executá-lo, certifique-se de que já tenha as bibliotecas necessárias instaladas.([Instale as bibliotecas necessárias](#instale-as-bibliotecas-necessárias))

## Executando:

Dentro do diretório da aplicação **form_site_example** execute:

```
$ flask run --debug
```

Um servidor na porta 5000 será iniciado e a URL estará no corpo da mensagem que irá aparecer na execução:

```
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 785-006-027
```

No ato de execução um pequeno banco de dados sqlite será criado dentro deste mesmo diretório, para simular um sistema de formulário real. O arquivo possui a extensão *.db

Pressione CTRL+C para finalizar o processo da aplicação servidora.
