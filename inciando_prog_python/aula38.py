#for com outro for dentro
# usando o i para a linha e o j para a coluna
for i in range(10):
    if i == 5:
        print('i é 5, pulando...')
        continue

    if i == 9:
        print('i é 8, seu else não executará')
        break


    for j in range(1, 3):
        print(i, j)
else:
    print('For completo com sucesso!')