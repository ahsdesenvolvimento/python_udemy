"""
For + Range
range -> range(start, stop, step), step - de quantos em quantos n quer pular
"""
numeros = range(0, 1000, 25) # inicio em 0, até 1000 e pulando de 25 em 25

for numero in numeros: #variavel numero criada para guardar cada iteração de numeros
    print(numero)