"""
Exercício
Peça ao usuário para digitar seu nome - ok
Peça ao usuário para digitar sua idade - ok 
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome} - ok
        Seu nome invertido é {nome invertido} - ok
        Seu nome contém (ou não) espaços - ok
        Seu nome tem {n} letras - ok
        A primeira letra do seu nome é {letra} - ok
        A última letra do seu nome é {letra} - ok
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios." - ok
"""
"""
nome = input('Digite seu nome: ')
idade =  input('Digite sua idade: ')
encontrar = ' '


if (nome !='' and idade !=''):
    print(f'seu nome é {nome}')
    print(f'seu nome invertido é {nome[::-1]}')
    letras=(len(nome))
    print(f'seu nome contém {letras} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é: {nome[-1]}')
if(nome !='' and idade !='')and(encontrar in nome):
    print('Seu nome contém espaços')
if(nome !='' and idade !='')and(encontrar not in nome):
    print('Seu nome não contém espaços')
elif(nome =='' or idade ==''):
    print("Desculpe, você deixou campos vazios.")
"""

nome = input('Digite o seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')

    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome NÃO contém espaços')

    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print("Desculpe, você deixou campos vazios.")


    
