"""
Classe Ponto e Retangulo:
Faça um programa completo utilizando funções e classes que:

Possua uma classe chamada Ponto, com os atributos x e y.
Possua uma classe chamada Retangulo, com os atributos largura e altura.
Possua uma função para imprimir os valores da classe Ponto
Possua uma função para encontrar o centro de um Retângulo.
Você deve criar alguns objetos da classe Retangulo.
Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior esquerdo do retângulo, que deve ser um objeto da classe Ponto.

A função para encontrar o centro do retângulo deve retornar o valor para um objeto do tipo ponto que indique os valores de x e y para o centro do objeto.

O valor do centro do objeto deve ser mostrado na tela.

Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo.
"""

class Ponto:
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y

    def imprimeValores(self):
        print(f'Ponto ({self.x,self.y})')


class Retangulo:
    def __init__(self,largura = 0,altura = 0,ponto = Ponto()):
        self.largura = largura
        self.altura = altura
        self.verticePartida = ponto

    def mostraMedidas(self):
        print(f'Largura: {self.largura}, Altura: {self.altura}, Vértice de Partida: {self.verticePartida.x,self.verticePartida.y}')

    def encontraCentro(self):
        x = self.verticePartida.x + self.largura/2
        y = self.verticePartida.y + self.altura/2
        return Ponto(x,y)


def menu():

    ret = Retangulo()
    vertice = Ponto()

    while True:
        opcao = input('Digite [1] para mudar as medidas do Retângulo, [2] para imprimir seu centro ou [3] para mostrar as medidas do retângulo: ')

        if opcao == '1':
            mudaValores(ret)
        elif opcao == '2':
            ret.encontraCentro().imprimeValores()
        elif opcao == '3':
            ret.mostraMedidas()
        else:
            print('Opção inválida, tente novamente.')


def mudaValores(retangulo):
    retangulo.largura = int(input('Digite o valor da nova largura: '))
    retangulo.altura = int(input('Digite o valor da nova altura: '))
    retangulo.verticePartida.x = int(input('Digite o valor da coordenada X do vértice de partida: '))
    retangulo.verticePartida.y = int(input('Digite o valor da coordenada y do vértice de partida: '))


menu()






