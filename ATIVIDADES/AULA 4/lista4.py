#Não devem ser utilizadas estruturas de programação que não estejam nas aulas 3 e 4.

      #QUESTÃO A

print ("Olá, vocẽ irá iniciar a habituação do seu animal! Vamos lá?")
print ("Digite '1' para BARRA DA ESQUERDA, '2' para BARRA DA DIREITA e '0' para NENHUMA BARRA")

nenhumaBarra = 0
barra1esq = 1
barra2dir = 2
sim = 'S'
nao = 'N'

barra1esq = int (input("O Animal apertou ou se aproximou da barra 1? Digite '1' para SIM, e '0' para NÃO \n"))
barra2dir =  int(input("O Animal apertou ou se aproximou da barra 2? Digite '2' para SIM, e '0' para NÃO \n"))
nenhumaBarra = int(input("O animal não apertou nenhuma barra? Digite '0' \n"))
if (barra1esq==1):
	print('Foram adicionados 0,5ml de recompensa')
elif (barra2dir == 2):
	print('Foram adicionados 0,5ml de recompensa')
else: 
	print("Nenhuma recompensa foi adicionada, e a barra deve ser retirada para realização de uma nova tentativa") 

animalHabituado = str(input("O animal conseguiu realizar as 20 repetições dentro do tempo estipulado? Digite 'S' para SIM, e 'N' para NÃO \n"))
if (sim == 'S'):
    print ("O animal está apto para a próxima etapa")
elif (nao == 'N'):
    print ("Repita o exercicio de habituação")

#QUESTÃO B

#ii. Se a variável de aproximação diminuiu (animal aproximou), liberar 0,5ml de rec
#iii. Se animal tocou na barra 20x, retornar que o experimento passou para a próxima etapa
#iv. Se o som1 foi emitido e o animal tocou na barra esquerda, liberar 0,5ml de rec
#v. Caso contrário não liberar nada
#vi. Se o som2 foi emitido e o animal tocou na barra direita, liberar 0,5ml de rec
#vii. Caso contrário não liberar nada
#viii. Se o experimento foi realizado 50x em 30min, apresentar que o experimento seguirá para a próxima fase.

print ("Agora você irá realizar o regime de aproximações sucessivas! Vamos lá?")
print ("Para iniciar o animal será posicionado a 30cm da barra, ok?")
print ("Digite 's1' se o animal se APROXIMAR ou TOCAR na barra da ESQUERDA, 's2' se o animal se APROXIMAR ou TOCAR na barra da DIREITA, e 'N' para NENHUMA BARRA")

nenhumaBarra = 'N'
Som1BE = 's1'
Som2BD = 's2'

Som1BE = int(input("O Animal tocou da barra da ESQUERDA? Digite 's1' para SIM, e 'N' para NÃO \n"))
Som2BD =  int(input("O Animal tocou da barra da DIREITA? Digite 's2' para SIM, e 'N' para NÃO \n"))
nenhumaBarra = int(input ("O animal não apertou nenhuma barra? Digite 'N' \n"))

if (Som1BE == 's1'):
	print('Foram adicionados 0,5ml de recompensa')
elif (Som2BD == 's2'):
	print('Foram adicionados 0,5ml de recompensa')
else: 
	print("Nenhuma recompensa foi adicionada") 

animalHabituado = str(input("O animal conseguiu realizar as 50 repetições dentro dos 30minutos? Digite 'S' para SIM, e 'N' para NÃO \n"))
if (sim == 'S'):
    print ("O animal está apto para a próxima etapa")
elif (nao == 'N'):
    print ("Repita o exercicio de habituação")
