"""
Fatiamento de strings
 012345678 (indices positivos)
 Olá mundo (string)
-987654321 (indices negativos)
Fatiamento [i:f:p] [::] - i: inicio f: fim p: passo
Obs.: a função len retorna a qtd  - verificar tamanho de determinada string
de caracteres da str
"""
variavel = 'Olá mundo'
print(variavel[::-1])

# Americana
# 012345678
#-987654321
nova_variavel = 'Americana'
print(nova_variavel[3:6]) # pega do indice 3 ao 5 (sempre um antes do final definido "6")
print(nova_variavel[-9:-2])
print(nova_variavel[0:9:2]) #vai do indice 0 ao 8 de 2 em 2 (Aeiaa)
print(nova_variavel[::-1]) # inverte a ordem da string
print(len(nova_variavel)) # exibe o tamanho da string
print(len(nova_variavel[4:9])) # exibe o tamanho da string do indice 4 ao 9