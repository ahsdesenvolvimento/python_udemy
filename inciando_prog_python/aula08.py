#Receber dados do usuário através da função input
#input recebe os dados como uma string, portanto se precisar
#utilizar como números, é necessario fazer a conversão de tipo

# nome = input('Qual o seu nome? ')
# print(f'O seu nome é {nome}')

numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

print(f'A soma dos números é: {int_numero_1 + int_numero_2}')
print(f'A subtração dos números é: {int_numero_1 - int_numero_2}')
print(f'A multiplicação dos números é: {int_numero_1 * int_numero_2}')