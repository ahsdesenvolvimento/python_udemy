"""
Exercicio:
Faça uma lista de compras com listas
O usuário deve ter a posibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de indices inexistentes na lista

"""
import os

lista_compras = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('cls')
        item = input('Item: ')
        lista_compras.append(item)
                        
    elif opcao == 'a':
        indice_str = input(
            'Escolha o índice para apagar: '
        )

        try:
            indice = int(indice_str)
            del lista_compras[indice]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
    elif opcao == 'l':
        os.system('cls')

        if len(lista_compras) == 0:
            print('Nada para listar')

        for i, item in enumerate(lista_compras):
            print(i, item)
    else:
        print('Por favor, escolha i, a ou l.')
    
