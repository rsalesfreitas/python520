#!/usr/bin/python3

usuarios = []
for l in open('usuarios.csv'):
    nome, idade, email = l.split(',')
    usuarios.append({"nome" : nome.strip(), "email" : email.strip (), "idade" : int(idade.strip())})

def extrair (i):
    return i['nome']

usuarios = []

for u in sorted(usuarios):
    print(u['nome'])  


# Abrir o arquivo usuarios
# Separar os valores por ","
# E escrever na tela o dicionario:
# {"nome" : "Hector" : "idade" : 27, "email" : "hector.silva@4linux.com.br"}
# Remover os \n e espacos antes e depois de cada valor
# Converter a idade para "inteiro"
# Colocar todos os usuarios dentro de uma lista
# Percorrer essa lista, exibindo apenas o nome de cada um
