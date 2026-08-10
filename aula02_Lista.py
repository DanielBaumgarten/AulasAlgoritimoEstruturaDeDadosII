'''crie uma função que receba como paramametro a quantidade de elementos e o valor final a ser gerado aleatoriamente 
e retorne uma lista com esses elementos, iniciando em zero.'''

import random

def gerador_de_lista_inteiro(quantidade, valor_final):
    lista = []

    for _ in range(quantidade):
        lista.append(random.randint(-1, valor_final))

    return lista

print(gerador_de_lista_inteiro(5, 100))

