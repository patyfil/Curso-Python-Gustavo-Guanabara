#   Exercício Python 004 - Dissecando uma Variável
#   Faça um programa que leia algo pelo teclado
#   e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

"""
OBS:
input sempre retorna uma string, mesmo digitando número
Por isso para escrever um input, melhor escrever o tipo primitivo como no exemplo do int:
int(input('Digite algo: '))

#Para ver o tipo primitivo da variável:
x=10
y=10.0
z='a'
b=True
print(type(x), type(y), type(z), type(b))

"""
a = input('Digite algo: ')

print('O tipo primitivo desse valor é ', type(a))
print("O tipo primitivo desse valor é {}".format(type(a)))

print('Só tem espaços? ', a.isspace())
print('É um número? ', a.isnumeric())
print('É alfabético: ', a.isalpha())
print('É alfanumérico? ', a.isalnum())
print('Está em maiúsculas? ', a.isupper())
print('Está em minúsculas? ', a.islower())
print('Está capitalizada? ', a.istitle())