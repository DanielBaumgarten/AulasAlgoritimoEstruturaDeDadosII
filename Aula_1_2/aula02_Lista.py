'''crie uma função que receba como paramametro a quantidade de elementos e o valor final a ser gerado aleatoriamente 
e retorne uma lista com esses elementos, iniciando em zero.'''

import random

def gerador_de_lista_inteiro(quantidade, valor_final):
    lista = []

    for _ in range(quantidade):
        lista.append(random.randint(-1, valor_final))

    return lista

def bubble_sort(lista):
    n = len(lista)

    for i in range(n):
        trocou = False

        for j in range (0, n - i -1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                trocou = True
        if not trocou:
            break
    return lista

numeros = gerador_de_lista_inteiro(5,100)

print("Lista original: ", numeros)

lista_ordenada = bubble_sort(numeros)

print("Lista ordenada: ", lista_ordenada)

print(gerador_de_lista_inteiro(5, 100))

