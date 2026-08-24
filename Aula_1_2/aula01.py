'''Criar uma Classe chamada Argola, esta deverá ter dois atributos: valor: int e proximo: none.
Crie uma Classe chamada Pino, esta deverá ter o seguinte atributo de instância: argola: Argola
Você deverá adionar ao pino uma estrutura de dados de pilha com instâncias de argola.'''


class Argola:
    def __init__(self, valor: int):
        self.valor = valor
        self.proximo = None


class Pino:
    def __init__(self):
        self.argola = None  # topo da pilha

    def empilhar(self, nova_argola: Argola):
        nova_argola.proximo = self.argola
        self.argola = nova_argola

    def imprimir_argolas(self):
        atual = self.argola

        if atual is None:
            print("O pino está vazio.")
            return

        while atual is not None:
            print(atual.valor)
            atual = atual.proximo


# Exemplo de uso
pino = Pino()

pino.empilhar(Argola(10))
pino.empilhar(Argola(20))
pino.empilhar(Argola(30))

print("Argolas no pino:")
pino.imprimir_argolas()