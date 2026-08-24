from gerador_de_numeros_inteiros import lista_de_inteiros
from lista import Lista
from nodo import Nodo


def adicionar_numeros_na_lista(minha_lista):

    for numero in lista_de_inteiros:
        minha_lista.adicionar(
            Nodo(numero)
        )


lista_ED = Lista()

adicionar_numeros_na_lista(lista_ED)

print("\nLISTA ORIGINAL")
lista_ED.print()

lista_ED.ordena_selection()

print("\nLISTA ORDENADA - SELECTION SORT")
lista_ED.print()