"""
Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
"""

class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def mudarLado(self, novo_lado):
        self.lado = novo_lado

    def retornaLado(self):
        return self.lado

    def calculaArea(self):
        return self.lado*self.lado

quad = Quadrado(5)
print(quad.retornaLado())
quad.mudarLado(8)
print(quad.retornaLado())
print(quad.calculaArea())