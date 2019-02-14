#!/usr/bin/python3

arquivo = open ('usuarios.csv')
for l in open('usuarios.csv'):
    nome, idade, email = l.split(',')
    print ({
        "nome" : nome.strip(), 
        "idade" : idade.strip(), 
        "email" : email.strip()
        })

# Abrir o arquivo usuarios
# Separar os valores por ","
# E escrever na tela o dicionario:
# {"nome" : "Hector" : "idade" : 27, "email" : "hector.silva@4linux.com.br"}
# Remover os \n e espacos antes e depois de cada valor
# Converter a idade para "inteiro"
