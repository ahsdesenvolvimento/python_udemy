"""
Iterando strings com while
"""
"""
#       012345678910
# minha tentativa:
nome = 'André Sousa'  # Iteráveis
#      -10987654321
tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)
#print(nome[3])

nova_string = ''
#nova_string += '*A*n*d*r*é* *S*o*u*s*a'

contador = 0
while contador <= tamanho_nome:
    nova_string = (f'*'+nome[contador]+'*')
    print(f'{nova_string}')
    contador += 1
print(f'{nova_string}')

"""
#Iterando strings com while
"""
#       012345678910
# nome = 'André Sousa'  # Iteráveis
#      1110987654321
"""
# reposta correta:
nome = 'André Sousa'  # Iteráveis

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)