# Calcular o IMC -  indice de massa corporal

#Classificação do IMC:
#Menor que 18,5 - Abaixo do peso
#Entre 18,5 e 24,9 - Peso normal
#Entre 25 e 29,9 - Sobrepeso (acima do peso desejado)

#Cálculo do IMC:
#IMC=peso (kg) / altura (m) x altura (m)


nome = 'André Sousa'
altura = 1.74
peso = 59
imc = peso/(altura * altura)

print(nome, "possui ", altura, 'm' , "pesa " , peso , "Kg"
      , "e seu IMC é " ,imc)

#verificando se esta no peso normal, abaixo do peso ou com sobrepeso
#utilizando o IMC

if(imc<18.5):{
    print('Abaixo do peso')
}
elif (imc >=18.5 and imc <=24.9):{ 
    print('Peso normal')
} 
else: print ('Sobrepeso (acima do peso desejado)')
