"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
lista_a = [10, 20, 30]
lista_b = [40, 50, 60]
lista_c = lista_a + lista_b #pegando os valores da lista a e b e jogando na nova lista c
lista_a.extend(lista_b) # método extend - estende a lista a até a lista b , não é possivel jogar valor em nova variavel
print(lista_a)