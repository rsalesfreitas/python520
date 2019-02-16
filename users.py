#!/usr/bin/python3
def hprint():
    print('{0:.<4} {1:.<20} {2:.<40}'.format('ID', 'NOME', 'EMAIL'))

def fprint(i, u):
    print('{0:.<4} {1:.<20} {2:.<40}'.format(i, u['nome'], u['email'])) 

usuarios = []
for l in open('usuarios.csv'):
    nome, idade, email = l.split(',')
    usuarios.append({"nome" : nome.strip(), "email" : email.strip (), "idade" : int(idade.strip())})

hprint()
for i, u in enumerate(sorted(usuarios, key=lambda i : i['nome']), start=1):
    fprint(i, u)

# escrever os nomes e os emails de cada usuario da seguinte forma:
# hector .............. ..... hector.silva@4linux.com.br
# guilherme ........... ..... guilherme.seraofim@ig.com

# criar uma funcao para criar o cabecalho chamada hprint():
# Nome ................ email .............................
# criar uma funcao chamada fprint () que recebe esses dois
# parametros e retorna uma string da forma especifica a cima
# com a numeracao de cada linha
