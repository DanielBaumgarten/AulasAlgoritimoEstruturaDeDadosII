'''Busca Sequencial (busca por exaustão ou binaria)'''

'''Você deverá implementar um algotimo que execute a mesma função do método index() já implementado na estrutura de dados lista do python
    Crie uma função que receba como parâmetro uma lista e a informação a ser encontrada nesta lista
    Está função devera retornar a ´posição da lista onde a informação foi encontrada, ou retnar None, caso a informação não seja encontrada
'''



def buscar_indice(lista, valor):
    for indice, elemento in enumerate(lista):
        if elemento == valor:
            return indice

    return None

lista = [10, 20, 30, 40, 50]
10

11
print(buscar_indice(lista, 30)) # 2
12
print(buscar_indice(lista, 50)) # 4
13
print(buscar_indice(lista, 99)) # None