# 1. Sistema automatizador de atualização de e-mails de aposetados e pensionistas

O nome da coluna de resposta é "E-MAIL"

O sistema somente irá atualizar o e-mail se o valor na planilha for diferente do valor encontrado.

Os e-mails são salvos em caixa alta.

Caso o servidor ou o pensionista não tenha um e-mail cadastrado o e-mail será salvo na planilha como: "email_nao_cadastrado"

## 1.1 Informações do sobre os dados:

A coluna de referência para a atualização de e-mail dos aposentados é a coluna "CPF SERVIDOR".

A coluna de referencia para a atualização de e-mail dos pensionistas é a coluna "VÍNCULO PENSÃO (EDITADO)".

## 1.2 Informações sobre o arquivo de coordenadas:

A quantidade de coordenadas deve ser igual a 6.

1 - Coordenada do radio button de seleção de aposentados ou pensionistas.

2 - Coordenada do campo de identificação (cpf do servidor ou matricula do pensionista).

3 - Coordenada do botão de pesquisa.

4 - Coordenada do campo de selecao e-mail.

5 - Coordenada do botão de usuário.

6 - Coordenada do botão de atualizar endereço eletrônico.

## 1.3 Criar arquivo executável com Graphic User Interface: 

```bash
pyinstaller -w --onefile --paths .\venv\Lib\site-packages <main.py>
```

Autor: Bruno Luiz de Deus Adão
Github: https://github.com/brunoblda