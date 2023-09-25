"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
# Incrementei utilizando a biblioteca random
import random
import os  # biblioteca que permite realizar limpeza do terminal

palavra_secretas= ['calopsita', 'gato', 'cachorro', 'ovelha', 'zebra',\
                   'peixe', 'elefante', 'onça', 'tigre', 'macaco',\
                    'urubu', 'ariranha', 'morcego', 'leopardo']
palavra_secreta = random.choice(palavra_secretas) # A função choice(colection) devolve um item de uma coleção
letras_acertadas = ''
numero_tentativas = 0

print('JOGO ADVINHE A PALAVRA')

while True:
    
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue
   
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
    palavra_formada =''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print(palavra_formada)
    if palavra_formada == palavra_secreta:
        os.system('cls') # limpando o terminal
        print(f'PARABÉNS!! VOCÊ ACERTOU! A PALAVRA SECRETA ERA: "{palavra_secreta}"'
              f' VOCÊ ACERTOU EM {numero_tentativas} TENTATIVAS')
        letras_acertadas = ''
        numero_tentativas = 0
        palavra_secreta = random.choice(palavra_secretas)
        print("\nconsegue acertar a próxima palavra ??")
        print('\nADVINHE A PALAVRA SECRETA')
        print(f'dica a palavra possui {len(palavra_secreta)} letras')

        