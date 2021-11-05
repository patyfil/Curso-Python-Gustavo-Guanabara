#   Exercício Python 010 - Conversor de Moedas
#   Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
#   e mostre quantos dólares ela pode comprar. Considere US$1,00 = 3,27
'''
real = float(input('Quanto dinheiro(reais R$) você tem na carteira? R$: '))
print(f'Com R${real} você pode comprar US${real/3.27:.2f}')
'''

real = float(input('Quanto dinheiro(reais R$) você tem na carteira? R$: '))
dolar = real / 5.61
euro = real / 6.48
print(f'Com R${real} você pode comprar US${dolar:.2f} ou €{euro:.2f}')


