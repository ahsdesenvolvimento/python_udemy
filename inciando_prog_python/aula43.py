"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['André', 'Renata', 1, True, 1.2]
lista_b = lista_a.copy() #copia a lista a em lista b

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)

"""
lista é um iteravel
for in com listas

"""
lista = ['André', 'Renata', 'Yellow']

for nome in lista:
    print(nome, type(nome))