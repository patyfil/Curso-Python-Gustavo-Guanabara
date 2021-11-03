#   Exercício Python 005 - Antecessor e Sucessor
#   Faça um programa que leia um número Inteiro
#   e mostre na tela o seu sucessor e seu antecessor.

"""
n = int(input('Digite um Número: '))
sucessor = n + 1
antecessor = n - 1

print('Analisando o valor {},\nO seu antecessor é: {},\nO seu Sucessor é: {}'.format(n, antecessor, sucessor))
"""
n = int(input('Digite um Número: '))
print('Analisando o valor {},\nO seu antecessor é: {},\nO seu Sucessor é: {}'.format(n, (n-1), (n+1)))

