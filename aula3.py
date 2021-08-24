'''
----------------------------------------
----- Este é o meu primeiro programa
----------------------------------------
'''

print("hello world da aula 3")
# esta instrução faz aparecer o que esta na tela preta do pc

issoEUmaString = "qqr coisa entre aspas dupla"
naoENumeroESimString = "15"
istoEUmInteiro = 15
istoTambemEUmaString = "isabelle"
istoEUmNumeroReal = 15.3
istoEUmBooleano = True
print (issoEUmaString, naoENumeroESimString, istoEUmInteiro,istoTambemEUmaString, istoEUmNumeroReal, istoEUmBooleano)
print (type(issoEUmaString))
print (type(naoENumeroESimString))
print (type(istoEUmInteiro))
print (type(istoTambemEUmaString))
print (type(istoEUmNumeroReal))
print (type(istoEUmBooleano))

import math

print(math.sqrt(100))

# import math
from math import sqrt

resultadosoma = 3+5 #soma
print(resultadosoma) 
print(2-3,6*5,8/2) #subtração, multiplicação, divisão
print (7//2, 2**10, 7%2) #parte inteira, potenciação, resto da divisão

soma = 0
soma += 3; print(soma); soma= soma+3; print(soma)
