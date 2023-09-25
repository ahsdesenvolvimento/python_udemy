""" while/else em Python"""
string = 'Valorqualquer'

i = 0 #index/indice
while i < len(string): #checando se o indice é menor que o tamanho da string
    letra = string[i]

    if letra == ' ':
        break

    print(letra)
    i += 1
else:
    print('Não encontrei um espaço na string.')
print('Fora do while.')