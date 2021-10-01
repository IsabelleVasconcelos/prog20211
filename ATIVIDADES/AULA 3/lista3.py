#FINALIZADO E EXECUTADO

#Microscopia confocal de varredura a laser
#A técnica de microscopia confocal de varredura à laser é 
#realizada a partir de um equipamento que lê informações 
#ópticas e devolve uma imagem. Porém, o equipamento em si 
#é desenvolvido de forma a interagir com usuários que inserem 
#informações e recebem informações a partir do dispositivo.

#Questão 2 
#OBS.: Não devem ser utilizadas estruturas de programação que
#      não estejam na aula 3.

#A) variáveis necessárias para que o programa funcione 
#corretamente.
from math import sqrt


varTipoDeMicroscopio = 'confocal' #confocal, biologico, fase
varResoluçãoDaImagem = '1024x768' #024 x 768, 800 x 600 e 320 x 240
varTipoDeCelula = 'nervosa' #nervosa, musular ou epitelial
varIluminacao = 300 #100 a 500
varFiltroDeLuz = 'vermelho' #vermelho, azul ou verde
varZoom = 20 #entre 0.5x e 40x
varArmazenamento = 'JPG' #PDF ou JPG
varAlturaDaLente = 'baixa' #alta, media ou baixa
varAberturaDaLente = 5 #1, 2, 3, 4 ou 5
varFoco = 10 #5um ,10um ou 15um

#C) Crie uma pequena mensagem de apresentação do programa para 
#realizar uma interface com o usuário.
print ('Esse programa tem como objetivo receber dados para realizar a analise microscopica confocal de varredura a laser')

msg = 'Houve alteração na variavel inserida?'

tmp1 = input("Qual o tipo de miscroscopio desejado? \n")
print (msg, varTipoDeMicroscopio != tmp1) # != compara o valor antigo com o digitado e diz se é verdadeiro ou falso / tmp diz sobre um valor temporario
varTipoDeMicroscopio = tmp1

tmp2 = (input("Qual a resolução de imagem desejada? \n")) 
print (msg, varResoluçãoDaImagem != tmp2)
varResoluçãoDaImagem = tmp2

tmp3 = (input("Qual o tipo de célula que irá ser estudado? \n"))
print (msg, varTipoDeCelula != tmp3)
varTipoDeCelula = tmp3

tmp4 = (input("Digite a iluminação desejada \n"))
print (msg, varIluminacao != tmp4)
varIluminacao = tmp4

tmp5 = (input("Qual a cor do filtro desejado? \n"))
print (msg, varFiltroDeLuz != tmp5)
varFiltroDeLuz = tmp5

tmp6 = (input("Digite o zoom desejado: \n"))
print (msg, varZoom != tmp6)
varZoom = tmp6

tmp7 = (input("Qual o formato que deseja armazenar o arquivo? \n"))
print (msg, varArmazenamento != tmp7)
varArmazenamento = tmp7

tmp8 = (input("Qual altura deseja configurar a lente? \n"))
print (msg, varAlturaDaLente != tmp8)
varAlturaDaLente = tmp8

tmp9 = (input("Digite a abertura de lente desejada: \n"))
print (msg, varAberturaDaLente != tmp9)
varAberturaDaLente = tmp9

tmp10 = (input("Qual o foco que deseja utilizar? \n"))
print (msg, varFoco != tmp10)
varFoco = tmp10

print (" As informações de configurações setadas foram: \n")
print ("Microscopio: ", tmp1)
print ("Resolução de imagem: ", tmp2)
print ("Tipo de célula: ", tmp3)
print ("Iluminação: ", tmp4)
print ("Filtro:", tmp5)
print ("Zoom:", tmp6)
print ("Local de armazenamento:", tmp7)
print ("Altura da lente: ", tmp8)
print ("Abertura da lente: ", tmp9)
print ("Foco: ", tmp10)


cal_hor = (input("Realize a calibração do equipamentto no sentido horizontal (Digite 10x a letra 'i' e, em seguinda, 10x a letra 'e'):  \n"))  
print ('A informação foi corretamente digitada: ', cal_hor)

cal_ver = (input("Realize a calibração do equipamento no sentido vertical (Digite 10x a letra 's' e, em seguinda, 10x a letra 'l'):  \n"))
print ('A informação foi corretamente digitada ', cal_ver)

print('A calibração foi concluída, tudo está pronto para iniciar a pesquisa :D')