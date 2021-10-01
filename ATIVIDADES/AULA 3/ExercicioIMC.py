#finalizado e executado

 #FAZER APENAS C TRUE OR FALSE
 
print("Olá! Vamos descobrir seu IMC?")

#varString = (imc = peso x altura**2):
#varFloat = (imc = peso x altura**2):

peso = float(input('Digite seu peso em Kg \n'))
print ('O peso informado:''peso em Kg')
altura = float (input('Digite sua Altura (m) \n '))
print ('Altura informada:''em M')
#(input ('insira seu nome e idade')

#import math
#print (imc)
#imc =(peso/altura**2)

#from math import imc
#print (imc=peso/altura*2)

import math
imc = (peso/altura**2) 
print ('seu imc é \n',imc)

print (imc <=17, "Muito abaixo do peso")
print (imc >17 <=18.5, "Abaixo do peso normal")
print (imc >18.5 <=25.0, "Peso dentro do normal")
print (imc >25 <=30, "Acima do peso normal")
print (imc >=30, "Muito acima do peso")

print ('fim :D')

#nesse caso não precisa usar o booleano  'varLogica1=true  /  varLogica2=false'