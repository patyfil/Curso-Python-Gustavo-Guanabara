#   Exercício Python 014 - Conversor de Temperaturas
#   Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

c = float(input('Informe a temperatura em °C: '))
f = c*1.8+32 #ou 9*c/5+32
print(f'A temperatura de {c} °C corresponde a {f}°F!')