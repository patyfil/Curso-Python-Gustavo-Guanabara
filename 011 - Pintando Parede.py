#   Exercício Python 011 - Pintando Parede
#   Faça um programa que leia a largura e a altura de uma parede em metros,
#   calcule a sua área e a quantidade de tinta necessária para pintá-la,
#   sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

lar = float(input('Digite a Largura da parede em metros: '))
alt = float(input('Digite a Altura da parede em metros: '))
area = lar * alt
tinta = area / 2

print(f'Sua parede tem a dimensão de {lar}m² x {alt}m² e sua área é de {area}m².\nPara pintar essa parede, você precisará de {tinta} litros de tinta')

