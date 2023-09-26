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
#        0   1   2   3
lista = [10, 20, 30, 40]
lista.append('André') # adiciona valor na última posição da lista
nome = lista.pop() # deleta último item da lista e salva valor deletado na variavel criada
lista.append(1233) 
del lista[-1] # deleta o valor que esta no indice -1 na lista
# lista.clear()
lista.insert(100, 5) # insert serve para inserir valor em determinado indice (posição / valor)
# se colocar indice que não existe na lista ele inseri na última posição
print(lista[4])
print(nome)