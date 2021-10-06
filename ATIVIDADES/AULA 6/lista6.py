#INCOMPLETO
# As entradas (seja informações de máquina, posicionamentos a serem medidos etc.) serão traduzidas em inputs no programa.

# O detalhamento das etapas é informado na tela para o usuário a cada passo do procedimento. FAZER  o comando PRINT  DE  CADA  PROCEDIMENTO

#O programa deve conter estruturas de tomada de decisão (if-elif-else). -> AULA  4

# O programa deve conter estruturas de repetição (while-for). ->  AULA  6

# O programa deve conter pelo menos 1 variável de cada tipo (lista, tupla e dicionário)
#( lista () coleção  ordenada  USA  COLCHETES ), 
# tupla { sequencia  de  valores , USA  PARENTESES } e
# dicionário { mapeamento  entre  uma {} chaveKEY  e  algum  conteudoVALUE }) - >  AULA  5


#INICIO
print ("Olá! Aqui vão as orientações para a realização da cirurgia! Siga o planejamento orientado")

#PROCESSO DE ANESTESIA
print ("Vamos iniciar o procedimento da anestesia ...")
tipoDeAnestesico = ['Ketamina e xilazina','Halotano' ]
print("Esses são os tipos de Anestesico disponiveis:") 
print(tipoDeAnestesico)
print("Selecione o tipo de anestesia que você se planejou para USAR:")
botaoApertado = int(input("Digite '1' se você deseja usar Ketamina e xilazina ou '2' para usar Halotano (gasoso)\n")) #1miligrama por kg
# botao2Apertado= int(input("Digite '2' se vocẽ deseja usar Halotano (gasoso).\n")) #5%kg

if (botaoApertado == 1):
    anestesico=tipoDeAnestesico[0]
    print('Anestesico:'+ anestesico)
    print ('agora que você escolheu o procedimento de anestesia verifique a dosagem correta de acordo com o peso do animal')
    print('A quantidade de anestesico é um mg por kg')
    peso = float(input('Digite o peso do seu animal em kg\n'))
    doseDeAnestesico = peso*0.001 #tantoxtantogramas escrever a funcaao'  
    print ('a dose de anestesico a ser  utilizada é \n',doseDeAnestesico)
     #calculo baseado na escolha 1
elif (botaoApertado == 2):
    anestesico=tipoDeAnestesico[1]
    print('Anestesico:'+ anestesico)
    print('A quantidade de anestesico é um mg por kg')
    peso = float(input('Digite o peso do seu animal em kg\n'))
    doseDeAnestesico = peso*0.05 #tantoxtantogramas escrever a funcaao'  
    print ('a dose de anestesico a ser  utilizada é \n',doseDeAnestesico)
     #calculo baseado na escolha 2
else: 
    print('Opção inválida')

#colocar um while para interrupção do ciclo
while (botaoApertado): 
  print ( "Fim do processo de anestesia" )
else: 
  print ('Repita a seleção do tipo de anestesico')

  #PROCESSO DE CPÇPCAR O ANIMAL NO ESTEREOTÁXICO
# Depois do anestésico ter feito efeito, deve-se posicionar o animal no estereotáxico.
# As barras que suportam o peso do animal devem ser posicionadas no ouvido externo do animal.
# Normalmente o animal dá uma pequena piscada, devido ao estímulo da musculatura responsável por este movimento.
# Em seguida verificar a angulação da cabeça do animal, a qual deve estar sem diferenças de angulação entre o bregma e o lambda, para ter uma superfície de cirurgia plana.


  #PROCEDIMENTO DE LIMPEZA DO CAMPO DE TRABALHO
print ('Agora você realizará a limpeza do campo de trabalho, esté procedimento requer o cumprimento de algumas etapas')
# Retirada da pelagem que recobre a parte superior da calota craniana, 
# Retirada dos tecidos moles (epiderme, derme e tecido conjuntivo) até alcançar a parte óssea da caixa craniana.
#  Por último e não menos importante deve-se limpar a calota craniana de qualquer resto de “pele” que esteja sobrando utilizando H2O2 10 volumes.
#pequena camada de poliacrilato em todo o perímetro externo para evitar sangramentos.

  #ESCOLHA DO PONTO DE FIXAÇÃO
#Após este procedimento deve-se escolher um ponto para a fixação de parafusos, de preferência na parte posterior da calota craniana, pois a camada óssea é mais espessa e suporta uma maior profundidade do parafuso.
print("Obs: Cuidar para não aprofundar muito o parafuso. Com parafusos maiores deve-se dar até 3 voltas no parafuso.")

  #POSICIONAMENTO DA AGULHA
print("Agora você irá posicionar a agulha sobre o bregma, realizando os calculos de posicionamento AnteroPosterior (AP), LateroLateral (LL) e DorsoVentral (DV)")
print('Insira os valores utilizados para os cálculos são os valores encontrados nas réguas a partir do posicionamento da agulha')

AnteroPosterior = float(input("Insira o valor de Antero Posterior: \n"))
LateroLateral1 = float(input("Insira o valor de Latero Lateral do hemisferio escolhido para colocar a primeira cânula: \n"))
LateroLateral2 = float(input("Insira o valor de Latero Lateral 2: \n"))
DorsoVentral = float(input("Insira o valor de Dorso Ventral: \n"))

AnteroPosterior = AnteroPosterior - 0,42  
LateroLateral1 = LateroLateral1 + 0,30
LateroLateral2 = LateroLateral2 - 0,30
DorsoVentral = DorsoVentral - 0,20

print('Esses são os valores a serem utilizados para localizar os pontos de inserção das cânulas-guia')
print(AnteroPosterior)
print(LateroLateral1)
print(LateroLateral2)
print(DorsoVentral)
print("Realize o posicionamento das cânulas-guia")

print('Depois de posicionar a agulha, fazer um furo com a broca até alcançar as meninges. A não perfuração das meninges é o procedimento ideal, e para conseguir isso apoie a mão que segura a broca contra o assoalho ou ao estereotáxico e perfure o crânio a +- 45° de angulação.')
print('Após ter atingido este objetivo, introduza a cânula-guia previamente confeccionada até o valor DorsoVentral (4,00) que foi calculado anteriormente.')
print("Logo após drenar qualquer sangue ou líquido cefalorraquidiano que esteja saindo pelo orifício criado no crânio. Para isso utilize pequenos rolos de papel absorvente.")
print ("aça uma mistura do acrílico polimerizante com o solvente até ficar com textura espessa porém maleável (o ideal é que a mistura seja capaz de cobrir a parte desejada sem escorrer por todo o crânio). Com essa mistura faça um capacete abrangendo o crânio, a cânula-guia e o parafuso. Deixe secar até ficar suficientemente rígido. O tempo de secagem varia de acordo com a temperatura e umidade da sala. ")
print ('O próximo passo é a fixação da outra cânula-guia. Deve-se levantar levemente o braço do estereotáxico cuidando para que a cânula-guia previamente fixada não se movimente. Logo após, posicionar a agulha sobre o outro ponto de inserção da cânula-guia. Introduzir a cânula-guia até o valor DV (4,00) calculado previamente.')







