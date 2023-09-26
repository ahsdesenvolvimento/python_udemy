"""
Introdução ao empacotamento e desempacotamento
"""
_, _, nome, *resto = ['Maria', 'Helena', 'Luiz'] # _ indica que exite uma váriavel que não sera utilizada / *resto variavel para guardar resto dos itens da lista
print(nome)


"""
Tipo tupla - Uma lista imutável
"""
nomes = ('André', 'Renata', 'Belinha') # túplas não fica entre [] e não pode ser alterado
# nomes = tuple(nomes) # transforma lista em tupla
# nomes = list(nomes) # transforma tupla em lista
print(nomes[-1])
print(nomes, type(nomes))