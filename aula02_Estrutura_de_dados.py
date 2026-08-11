class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class Lista:
    def __init__(self):
        self.inicio = None

    def adicionar(self, valor):
        novo_no = No(valor)

        if self.inicio is None:
            self.inicio = novo_no
            return

        atual = self.inicio

        while atual.proximo is not None:
            atual = atual.proximo

        atual.proximo = novo_no

    def index(self, valor):
        atual = self.inicio
        posicao = 0

        while atual is not None:
            if atual.valor == valor:
                return posicao

            atual = atual.proximo
            posicao += 1

        return None

    def exibir(self):
        atual = self.inicio

        while atual is not None:
            print(atual.valor, end=" -> ")
            atual = atual.proximo

        print("None")

        lista = Lista()

        lista.adicionar(10)
        lista.adicionar(20)
        lista.adicionar(30)
        lista.adicionar(40)

        lista.exibir()

        print(lista.index(30))  # 2
        print(lista.index(40))  # 3
        print(lista.index(99))  # None