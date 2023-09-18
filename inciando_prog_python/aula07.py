#formatação de strings

nome = 'André Sousa'
altura = 1.74
peso = 59
imc = peso / altura ** 2

"f-strings"
linha_1 = f'{nome} tem {altura:.2f} de altura,' #colocar variavel entre chaves
linha_2 = f'pesa {peso} quilos e seu imc é' #começar com f e colocar tudo dentro de aspas
linha_3 = f'{imc:.2f}' # utilizando :.2f define-se as casas decimais 

print(linha_1)
print(linha_2)
print(linha_3)

# André Sousa tem 1.74 de altura,
# pesa 59 quilos e seu IMC é
# 19.487382745408905

# Formatando com a função (método) format

a = 'AAAAA'
b = 'BBBBBB'
c = 1.1
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}' #parametro nomeado a={nome1}
formato = string.format(
    nome1=a, nome2=b, nome3=c
)

print(formato)