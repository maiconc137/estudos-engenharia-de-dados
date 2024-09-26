# Enunciado do Exercício:
# 
# Escreva um programa em Python que calcule a quantidade de latas de tinta necessárias para pintar uma parede. 
# O usuário deverá fornecer as seguintes informações:
#
# - Rendimento da tinta (em metros quadrados por litro): a quantidade de área que uma lata de tinta pode cobrir.
# - Altura da parede (em metros).
# - Largura da parede (em metros).
#
# O programa deve calcular a área total da parede e, em seguida, determinar quantas latas de tinta serão necessárias, considerando o rendimento informado pelo usuário.
#
# Fórmula:
# Área da parede é calculada como:
# Área = Altura x Largura
#
# A quantidade de latas de tinta será dada por:
# Latas necessárias = Área / Rendimento
#
# Exemplo de uso:
# Informe o rendimento da tinta (m² por lata): 10
# Informe a altura da parede (m): 2.5
# Informe a largura da parede (m): 4
#
# Você necessita de 1 lata(s) de tinta.
#
# O programa deve arredondar o número de latas para cima, já que não se pode comprar meia lata de tinta.

# Escreva o código abaixo:

from math import ceil

redimento_tinta_informado = int(input('Rendimento: '))
altura = int(input('Altura: '))
largura = int(input('Largura: '))

area = altura * largura

redimento_tinta = area / redimento_tinta_informado

print(ceil(redimento_tinta))  # Arredondado para cima
print(redimento_tinta)  # Valor original
