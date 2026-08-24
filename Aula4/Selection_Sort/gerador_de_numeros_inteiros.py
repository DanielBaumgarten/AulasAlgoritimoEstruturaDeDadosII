import random


def lista_inteiros(
        tamanho_lista: int = 10,
        intervalo_maximo: int = 100
) -> list:

    lista = random.sample(
        range(0, intervalo_maximo),
        tamanho_lista
    )

    return lista


lista_de_inteiros = lista_inteiros()