"""
Formatação de strings utilizando o f-strings f'{variavel}'
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda (preencher para a esquerda)
< - Direita (preencher para a direita)
^ - Centro (preencher no centro)
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}') #preenche a esquerda com espaço até chegar a 10 caracteres
print(f'{variavel: <10}.') #preenche a direita com espaço até chegar a 10 caracteres
print(f'{variavel: ^10}.') #preenche no centro com espaço até chegar a 10 caracteres
print(f'{1000.4873648123746:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')