#   Exercício Python 006 - Dobro, Triplo, Raiz Quadrada
#   Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

"""
n = int(input("Digite um número: "))
dobro = n + n
triplo = n * 3
raizq = pow(n, (1 / 2))

print('O dobro do número {}, vale {}, O triplo vale {}, A raiz quadrada é igual a {}'.format(n, dobro, triplo, raizq))

"""

n = int(input("Digite um número: "))
print('O dobro do número {} vale {}, O triplo vale {}, A raiz quadrada de {} é igual a {}'.format(n, n*2, n*3, n, n**(1/2)))
