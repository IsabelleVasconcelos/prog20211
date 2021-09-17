#não estou entendendo mais nada

# copiarslide16aqui
classif  =  OneVsRestClassifier ( estimador = SVC ())
modeloTreinado  =  classif . ajuste ( x , y )
yestimado  =  modeloTreinado . prever ( x )

#validacao
x = [[ 4 , 2 ], [ 7 , 4 ], [ 4 , 9 ], [ 3 , 3 ], [ 3 , 0 ]]
y = [ 1 , 8 , 1 , 3 , 2 ]
yestimado  =  modeloTreinado . prever ( x )
imprimir ( y , yestimado , y == yestimado )



de  sklearn  import  svm
de  sklearn . conjuntos de dados  import  load_digits
import  matplotlib . pyplot  como  plt

digits  =  load_digits ()
plt . cinza ()
para  imagens  em  dígitos . imagens :
  plt . matshow ( imagens )
  plt . show ()
classif  =  svm . SVC ( gama = 0,001 , c = 100. )
modeloTreinado  =  classif . ajuste ( dígitos . dados [: - 1 ], dígitos . alvo [: - 1 ])
predizer  =  modeloTreinado . prever ( dígitos . dados [: - 1 ])
imprimir ( prever )

images_and_predictions  =  list ( zip ( dígitos [ - 1 :], prever ))
para  índice , ( imagem , previsão ) em  enumerar ( imagens_and_predictions ):
  plt . eixo ( 'desligado' )
  plt . imshow ( imagem )
  imprimir ( previsão )
  
  #deu erro, e ai eu me perdi. assistir a aula novamente
  
  
  de  sklearn  import  svm
  de  conjuntos de dados de importação sklearn  
  classif  =  svm . SVC ( gama = 'escala' )
  íris  =  conjuntos de dados . load_iris ()
  x , y  =  íris . dados , íris . alvo
  modeloTreinado  =  classif . ajuste ( x , y )
  imprimir ( y [ 51 ])
  
  de  despejo de importação de joblib  , carregar 
  despejo ( modeloTreinado , 'modeloTreinado.mod' )
  
  clf  =  load ( 'modeloTreinado.mod' )
  imprimir ( clf . predizer ([ x [ 51 ]]))


  #pos intervalo - nao entendi mais nada - reassitir