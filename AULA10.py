
#copiarslide16aqui
classif = OneVsRestClassifier(estimator=SVC())
modeloTreinado = classif.fit(x,y)
yestimado = modeloTreinado.predict(x)

#validacao
x= [[4,2],[7,4],[4,9],[3,3],[3,0]]
y= [1,8,1,3,2]
yestimado = modeloTreinado.predict(x)
print(y,yestimado,y==yestimado)



from sklearn import svm
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt

digits = load_digits()
plt.gray()
for imagens in digits.images:
  plt.matshow(imagens)
  plt.show()
classif = svm.SVC(gamma=0.001, c=100.)
modeloTreinado = classif.fit(digits.data[:-1],digits.target[:-1])
predict = modeloTreinado.predict(digits.data[:-1])
print(predict)

images_and_predictions = list(zip(digits[-1:],predict))
for index, (image,prediction) in enumerate(imagens_and_predictions):
  plt.axis('off')
  plt.imshow(image)
  print(prediction)
  
  #deu erro, e ai eu me perdi. assistir a aula novamente
  
  
  from sklearn import svm
  from sklearn import datasets
  classif = svm.SVC(gamma='scale')
  iris = datasets.load_iris()
  x, y = iris.data, iris.target
  modeloTreinado = classif.fit(x,y)
  print(y[51])
  
  from joblib import dump, load
  dump(modeloTreinado, 'modeloTreinado.mod')
  
  clf = load('modeloTreinado.mod')
  print(clf.predict([x[51]]))
  
  
  #pos intervalo - nao entendi mais nada - reassitir
