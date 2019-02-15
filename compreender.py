#!/usr/bin/python3

# Transformar o double em lambda

def double(i):
    return i*2

for n in map (lambda i : i *2, [1, 2, 3, 4]):
    print (n)

duck_tails = ['huguinho|1', 'Zezinho|2', 'Luizinho|3']

# percorrer a variavel duck_tails
# e exibir apenas os nomes, sem os numeros
# ao inves de escrever o nome todo
# escrever a primeira e a ultima letra de cada nome
# nao escrever quando o nome for zezinho

for d in [i.split('|')[0] for i in duck_tails]:

    print(d[0], d[-1])


