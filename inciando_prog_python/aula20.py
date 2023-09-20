"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
"""
numero_str = input(
    'Vou dobrar o número que vc digitar: '
)

try:
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')


# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
# else:
#     print('Isso não é um número')
"""

print ("Realizarei a divisão dos números que serão digitados")
numero_um = input('Digite o primeiro numero: ')
numero_dois = input ('Digite o segundo número: ')

try:
    num_um = float(numero_um) #trasformando a string númerica em float
    num_dois = float(numero_dois)
    print(f'{numero_um} dividido por {numero_dois} é : {num_um/num_dois:.2f}')
except:
    print("Você não digitou números ou tentou dividir por 0")