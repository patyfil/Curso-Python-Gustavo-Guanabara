#Exercício Python 008 - Conversor de Medidas
#Desafio 8 – Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
#Os múltiplos do metro são quilômetro (km), hectômetro (hm) e decâmetro (dam),
#e os submúltiplos são decímetro (dm), centímetro (cm) e milímetro (mm).
# km hm dam m dm cm mm

"""
medida = float(input('Digite uma distância em metros: '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print(f'A medida de {medida} metros corresponde a {cm} em centímetros e {mm} em milímetros')
print(A medida de {} corresponde a {:.0f}cm e {:.0f}mm'.format(medida, cm, mm))

"""

medida = float(input('Digite uma distância em metros: '))
print(f'A medida de {medida} metros corresponde a {medida * 100} em centímetros e {medida * 1000} em milímetros')
print('km =', medida/1000)
print('hm =', medida/100)
print('dam =', medida/10)
print(f'dm = {medida*10:.0f}')
print(f'cm = {medida*100:.0f}')
print(f'mm = {medida*1000:.0f}')