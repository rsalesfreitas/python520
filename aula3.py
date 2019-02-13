#!/usr/bin/python3

arquivo = open('zen.txt')

# mod -> 1 % 2

#for linha in arquivo:
#    linha = linha.strip()
#     if i % 2 == 0:
#    if linha != '-':
#        print(linha)

#if linha in (arquivo) -> ('-')
#print(linha, '-')

for i, linha in enumerate(arquivo):
    if i % 2 == 0:
        print (linha.strip())
