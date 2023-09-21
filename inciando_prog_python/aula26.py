"""
Operadores de atribuição
= += -= *= /= //= **= %=
"""
"""
contador = 10

###

contador /= 5
print(contador)
cont= 0
nome1 = ''
nome2 = ''
nome3 = ''
"""
cont = 0
while cont <3:
    cont += 1 # ao inves contador = contador+1
    nome = input('digite seu nome: ')
    if cont == 1:
        nome1 = nome
    elif cont == 2:
        nome2 = nome
    elif cont == 3:
        nome3 = nome
print(f'o primeiro nome é {nome1}')
print(f'o segundo nome é {nome2}')
print(f'o terceiro nome é {nome3}')