# Projeto CRUD de Músicas em Python

Projeto desenvolvido para a disciplina de Programação Orientada a Objetos do curso de Engenharia de Dados da Ada Tech em parceria com o Santander Coders.
Este projeto é uma aplicação simples para gerenciar um catálogo de músicas usando Programação Orientada a Objetos (POO) em Python. 
A aplicação permite criar, ler, atualizar e deletar (CRUD - Create Read Update Delete) registros de músicas, utilizando arquivos de texto para persistência dos dados.

## Estrutura do Projeto

O projeto é dividido em dois arquivos principais:
1. `data_music.py`: Contém a classe DataMusic, responsável pelas operações CRUD (Create, Read, Update, Delete) e manipulação dos dados das músicas.
2. `interface.py`: Fornece uma interface de linha de comando para interagir com a classe *DataMusic*.

### data_music.py

Este arquivo define a classe *DataMusic* que realiza as seguintes operações:
- `create(id_musica, nome, banda)`: Adiciona uma nova música ao arquivo, se o ID não existir.
- `read(id_musica)`: Retorna os detalhes da música com o ID fornecido.
- `update(id_musica, nome=None, banda=None)`: Atualiza os detalhes da música com o ID fornecido.
- `delete(id_musica)`: Remove a música com o ID fornecido.
- `list_musicas()`: Lista todas as músicas armazenadas.

### interface.py

Este arquivo fornece uma interface de linha de comando para o usuário interagir com o sistema. O menu apresenta opções para criar, ler, atualizar, deletar e listar músicas.

## Executando o Projeto

1. Criar o Arquivo de Dados:

Antes de executar o script da interface, certifique-se de que o arquivo de dados musicas.txt está presente no mesmo diretório. Se o arquivo não existir, o sistema o criará automaticamente ao adicionar a primeira música.

2. Executar o Script da Interface:

Execute o script `interface.py` para iniciar a aplicação e interagir com o sistema:

```
python interface.py
```
3. Interagir com o Menu:

Use o menu apresentado para criar, ler, atualizar, deletar e listar músicas. Siga as instruções fornecidas no terminal para gerenciar as músicas no sistema.

## Considerações

- *Persistência de Dados:* Os dados são armazenados em um arquivo de texto (musicas.txt), e a manipulação é feita manualmente sem uso de bibliotecas externas.
- *Funcionalidade:* A aplicação permite uma gestão básica de músicas, adequada para uso simples e testes.
