class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class Lista:
    def __init__(self):
        self.inicio = None

    def adicionar(self, valor):
        novo_nodo = Nodo(valor)

        if self.inicio is None:
            self.inicio = novo_nodo
            return

        atual = self.inicio

        while atual.proximo is not None:
            atual = atual.proximo

        atual.proximo = novo_nodo

    def localizar(self, valor):
        atual = self.inicio
        posicao = 0

        while atual is not None:
            if atual.valor == valor:
                return {
                    "elemento": atual.valor,
                    "posicao": posicao
                }

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

resultado = lista.localizar(30)

if resultado:
    print(
        f"Elemento encontrado: {resultado['elemento']} "
        f"na posição {resultado['posicao']}"
    )
else:
    print("Elemento não encontrado.")