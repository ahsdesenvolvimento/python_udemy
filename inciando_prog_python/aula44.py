"""
Exercicio 
Exiba os indices da lista
0 - André
1 - Renata
2 - Yellow
"""

lista = ['André', 'Renata', 'Yellow']
lista.append('Ariel')
indices = range(len(lista))

for indice in indices:
    print(indice,lista[indice])
