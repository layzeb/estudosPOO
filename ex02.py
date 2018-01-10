"""
Classe Retangulo: Crie uma classe que modele um retangulo:

Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e
calcular Perímetro;
Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe
as medidades de um local. Depois, deve criar um objeto com as medidas e calcular
a quantidade de pisos necessárias para o local.
"""

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def mudarLados(self, nova_base, nova_altura):
        self.base = nova_base
        self.altura = nova_altura

    def retornarLados(self):
        return self.base, self.altura

    def calculaArea(self):
        return self.base*self.altura

    def calculaPerimetro(self):
        return self.base*2 + self.altura*2

comprimento = float(input('Informe o comprimento do local em metros: '))
largura = float(input('Informe a largura do local em metros: '))

piso_comp = float(input('Informe o comprimento do piso em metros: '))
piso_larg = float(input('Informe a largura do piso em metros: '))

local = Retangulo(comprimento,largura)
print(f'A área do local é {local.calculaArea()} metros quadrados.')

piso = Retangulo(piso_comp,piso_larg)
#print(f'A área de um azulejo é {piso.calculaArea()} metros quadrados.')

qtd = round(local.calculaArea() // piso.calculaArea())

print(f'A quantidade de piso para o local é de {qtd}')
