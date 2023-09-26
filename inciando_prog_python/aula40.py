"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""
#        +01234
#        -54321
#string = 'ABCDE'  # 5 caracteres (len)
# print(bool([]))  # falsy
# print(lista, type(lista))

#        0    1      2              3    4
#       -5   -4     -3             -2   -1
#lista = [123, True, 'André Sousa',  1.2, []]
#lista[-3] = 'Renata'
#print(lista)
#print(lista[2], type(lista[2]))

"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3   4   5
lista = [30, 50, 70, 90]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])
lista.append(50) # adiciona valor a última posição da lista
lista.pop() # remove último indice da lista
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop(3) # informando o indice dentro de () no pop é possivel remover o indice especificado
print(lista, 'Removido,', ultimo_valor) # exibindo valor removido