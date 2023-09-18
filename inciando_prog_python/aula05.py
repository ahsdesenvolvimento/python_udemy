#Operadores Aritméticos

adicao = 10 + 10
print('Adição', adicao)

subtracao = 10 - 5
print('Subtração', subtracao)

multiplicacao = 10 * 10
print('Multiplicação', multiplicacao)

divisao = 10 / 3  # sempre o retorno é float
print('Divisão', divisao)

divisao_inteira = 10 // 2 # corta as casas decimais 
print('Divisão inteira', divisao_inteira)

exponenciacao = 2 ** 10 # potencia
print('Exponenciação', exponenciacao)

modulo = 55 % 2  # resto da divisão
print('Módulo', modulo)

print(10 % 8 == 0) #verificar se 10 é divisivel por 8
print(16 % 8 == 0) #verificar se 16 é divisivel por 8
print(10 % 2 == 0) #verificar se 10 é par (divisivel por 2)
print(15 % 2 == 0) #verificar se 15 é par (divisivel por 2)
print(16 % 2 == 0) #verificar se 16 é par (divisivel por 2)
print(9 % 3 == 0)  #verificar se 9 é impar (divisivel por 3)

# Verificando se o número passado é par ou impar
numero = 3
if(2 % numero == 0):{
print("o número é par")
}
else : print ("O numero é impar")

# concatenação 

concatenacao = 'André' + ' ' + 'Sousa' # só pode ser string para concatenar
print(concatenacao)

a_dez_vezes = 'A' * 10 #sinal de multiplicação faz a repetição
tres_vezes_andre = 3 * 'André'
print(a_dez_vezes)
print(tres_vezes_andre)

# Precedencia entre operadores aritméticos
 
# 1. (n + n) primeiro resolve os parenteses
# 2. **      segundo resolve a exponenciação /  potenciação
# 3. * / // % terceiro resolve multiplicação / divisão e modulo
# 4. + - por ultimo a soma e subtração

# obs: caso os operadores tenham a mesma precedencia, será realizado
# primeiro da esquerda para a direita, de cima para baixo

conta_1 = (1 + int(0.5 + 0.5)) ** (5 + 5)
print(conta_1)

conta_2 = (1 * 9 + (1+9) + int(0.5 + 0.5)) ** (5 + 5)
print(conta_2)