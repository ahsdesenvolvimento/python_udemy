""" Calculadora com while """
#startswitch  - verifica se começa com determinada string, retorna bool
# minha tentativa:
while True:
    try:
        primeiro_numero = input('Digite o primeiro número: ')
        primeiro_numero_float = float(primeiro_numero)
        segundo_numero = input ('Digite o segundo número: ')
        segundo_numero_float = float(segundo_numero)
        operacao = input('escolha a operação: [1]SOMA, [2]SUBTRAÇÃO, [3]MULTIPLICAÇÃO, [4]DIVISÃO :')
        operacao_escolhida = int(operacao)

        soma = primeiro_numero_float + segundo_numero_float
        subtracao = primeiro_numero_float - segundo_numero_float
        multiplicacao = primeiro_numero_float * segundo_numero_float
        divisao = primeiro_numero_float / segundo_numero_float

         
        match operacao_escolhida:
            case 1:
                print(f'{primeiro_numero_float} + {segundo_numero_float} = {soma}')
            case 2:
                print(f'{primeiro_numero_float} - {segundo_numero_float} = {subtracao}')
            case 3:
                print(f'{primeiro_numero_float} X {segundo_numero_float} = {multiplicacao}')
            case 4:
                print(f'{primeiro_numero_float} / {segundo_numero_float} = {divisao}')
            case _:
                print("Opção invalida")
        
        
    except:
        print('você digitou valor inválido')

    #########
    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break

    # Solução do professor:

    """ Calculadora com while """
    
while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None # numeros inválidos

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True #numeros válidos
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    ###

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break
