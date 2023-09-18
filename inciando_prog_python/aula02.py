#print(12,34, sep='-') #argumento sep é para definir o tipo de separador
#print(12,34, sep='.',end='\n\n') #argumento end define o fim de linha
#print(1,4, sep='.',end='\n')

#tipos de dados
#str -  String -  texto dentro de aspas

#aspas simples
#print('Boa tarde'+'Fred')
#aspas duplas
#print("Olá mundo")
#escape - utilizar a \ para informar p/ ignorar o próximo caracter (não interpretar)
#print('Americana\'SP')
# r 
#print(r'Americana\'SP')
#print('Americana"SP"')

#função type mostra o tipo do dado - type é uma classe
#print ( type(1)) # inteiro
#print ( type('Teste')) #string 
#print ( type(1.1)) #float
#print ( type(True) ) #booleano

# conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
#  tipos imutáveis e primitivos:
# str, int, float, bool
#print(int('1'), type(int('1')))
#print(type(float('1') + 1))
#print(bool(' '))
#print(str(11) + 'b')

#variaveis: variavel_um - snake case , variavelUm -  Kamel case

# Variáveis são usadas para salvar algo na memória do computador.
# PEP8: inicie variáveis com letras minúsculas, pode usar
# números e underline _.
# O sinal de = é o operador de atribuição. Ele é usado para
# atribuir um valor a um nome (variável).
# Uso: nome_variavel = expressão

# nome_completo = 'André H'
# soma_dois_mais_dois = 2 + 2
# int_um = bool('1')
# print(int_um, type(int_um))
# print(nome_completo, soma_dois_mais_dois)

nome = 'André'
idade = 35
maior_de_idade = idade >= 18
print('Nome:', nome, 'Idade:', idade)
print('É maior?', maior_de_idade)