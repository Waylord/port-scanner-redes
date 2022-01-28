# PortScanner

A aplicação consiste em uma ferramenta que verifica uma lista de portas, no qual tenta estabelecer conexões e classificá-las de acordo com a resposta que é obtida pelo PortScanner.

## Objetivo

O projeto tem como objetivo avaliar vulnerabilidades de portas de conexões, através de classificações, onde possa ser identificadas como abertas, filtradas e fechadas. O projeto será utilizado como avaliação para a turma de Redes II para Sistemas de Informação pelo professor Flávio Luiz Seixas.

## Alunos

* Igor Castro
* Jair Ribeiro
* Millena Costa

## Pré-requisitos
* Python 3 (https://www.python.org/downloads/)

## Instruções
* Realize o download e instalação do Python
* Abra o prompt de comando e verifique se o Python está instalado corretamente, utilizando a função python --version.
* Clone o repositório para sua máquina local e execute o arquivo main.py

# Detalhes de implementação:

## Socket

Para fazer a conexão TCP entre as redes, utilizou-se a biblioteca socket.

## Threads

Para evitar a espera do timeout das chamadas em portas filtradas, implementou-se a opção de processamento paralelo (threading) utilizando a biblioteca nativa do Python, Threading.
 
## Execução 

O arquivo irá executar as seguintes portas durante o threading
* Thread 1: 20, 21, 22, 23, 25, 80 , 115, 443
* Thread 2: 514, 530, 547, 587, 636, 873
* Thread 3: 990, 992, 993, 995, 1433, 1521, 2049
* Thread 4: 2081, 2083, 3306, 8081, 8090, 5432, 5500
