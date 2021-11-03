#Desafio 7 – Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
#{:.1f} Depois do ponto flutuante coloque apenas 1 dígito
"""
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A média do aluno é igual a {}'.format(m))
"""

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
print(f'A média entre {n1:.2f} e {n2} é igual a {(n1+n2)/2:.3f}')