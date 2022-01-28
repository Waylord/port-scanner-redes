# PortScanner

Atividade de implementação da disciplina de Redes

## Objetivo

O programa deverá varrer essas portas tentando estabelecer conexões e, com base no resultado dessa tentativa, classificar cada porta da faixa. Ao final da execução, o programa deverá listar todas as portas abertas, todas as portas filtradas e todas as portas fechadas.

## Alunos

* Millena Costa
* Jair Lima
* Igor Castro

Detalhes de implementação:

## Socket

Para fazer a conexão TCP entre as redes, utilizamos a biblioteca socket.

## Threads

Para evitar a espera do timeout das chamadas em portas filtradas, foi implementada a opção de processamento paralelo¹ utilizando a biblioteca nativa do python threading.

## Execução 

Basta rodar a aplicação, todas as entradas necessárias já foram pre-definidas pelo grupo.
