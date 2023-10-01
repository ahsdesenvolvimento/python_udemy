"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

cpf = input('Digite 9 digitos: ')

while len(cpf) > 9 or len(cpf) < 9:
    print('Você deve digitar apenas 9 digitos')
    cpf = input('Digite 9 digitos: ')


    
#informe_cpf = '7,4,6,8,2,4,8,9,0'
#cpf = informe_cpf.split(',')

print(f'Você digitou o CPF: {cpf}')
soma_digitos = (int(cpf[0:1])*10)+(int(cpf[1:2])*9)+\
    +(int(cpf[2:3])*8)+(int(cpf[3:4])*7)\
    +(int(cpf[4:5])*6)+(int(cpf[5:6])*5)+(int(cpf[6:7])*4)\
    +(int(cpf[7:8])*3)+(int(cpf[8:9])*2)
#print(f'A soma dos digitos é : {soma_digitos}')
multiplicacao_resultado = soma_digitos * 10
#print(f'A multiplicação do resultado é : {multiplicacao_resultado}')
primeiro_digito_cpf = multiplicacao_resultado % 11
#print(f'O resto do valor dividido por 11 é : {primeiro_digito_cpf}')
if primeiro_digito_cpf > 9:
    primeiro_digito_cpf =0
print(f'O primeiro digito do CPF é : {primeiro_digito_cpf}')

"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""

soma_nove_digitos= (int(cpf[0:1])*11)+(int(cpf[1:2])*10)+\
    +(int(cpf[2:3])*9)+(int(cpf[3:4])*8)\
    +(int(cpf[4:5])*7)+(int(cpf[5:6])*6)+(int(cpf[6:7])*5)\
    +(int(cpf[7:8])*4)+(int(cpf[8:9])*3)+(primeiro_digito_cpf*2)
multiplicacao_resultado_2 = soma_nove_digitos * 10
segundo_digito_cpf = multiplicacao_resultado_2 % 11
if segundo_digito_cpf > 9:
    segundo_digito_cpf =0
print(f'O segundo digito do CPF é : {segundo_digito_cpf}')

"""
Solução do professor:

#cpf = '36440847007'  # Esse CPF gera o primeiro dígito como 10 (0)
cpf = '74682489070'
nove_digitos = cpf[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito_1 in nove_digitos:
    resultado_digito_1 += int(digito_1) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0
print(digito_1)

# cpf = '36440847007'  # Esse CPF gera o primeiro dígito como 10 (0)
cpf_enviado_usuario = '74682489070'
nove_digitos = cpf_enviado_usuario[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11

resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
    print(f'{cpf_enviado_usuario} é válido')
else:
    print('CPF inválido')

"""



