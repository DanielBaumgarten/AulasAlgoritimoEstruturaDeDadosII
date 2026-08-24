class Lista:

    def __init__(self):
        self.elemento = None
        self.fim = None

    def vazio(self):

        if self.elemento is None:
            return True

        return False

    def adicionar(self, novo_elemento):

        if self.vazio():
            self.elemento = novo_elemento
            self.fim = novo_elemento
            return

        self.fim.proximo = novo_elemento
        self.fim = novo_elemento

    def print(self):

        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

        elemento = self.elemento

        while elemento:

            print(
                f"End.Atual: {str(elemento)[-5:]} - "
                f"{elemento.valor} - "
                f"{str(elemento.proximo)[-5:]}"
            )

            elemento = elemento.proximo

    def index(self, valor):

        elemento = self.elemento

        while elemento:

            if elemento.valor == valor:
                return (
                    f"Valor {valor} encontrado "
                    f"no elemento {str(elemento)[-5:]}"
                )

            elemento = elemento.proximo

        return (
            f"Valor {valor} não encontrado "
            f"em nenhum elemento da lista"
        )

    def ordena_selection(self):

        atual = self.elemento

        while atual is not None:

            menor = atual
            proximo = atual.proximo

            while proximo is not None:

                if proximo.valor < menor.valor:
                    menor = proximo

                proximo = proximo.proximo

            if menor != atual:
                atual.valor, menor.valor = (
                    menor.valor,
                    atual.valor
                )

            atual = atual.proximo