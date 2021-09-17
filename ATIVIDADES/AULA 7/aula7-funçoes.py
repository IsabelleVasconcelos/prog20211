def nomeFuncao(entrada1_opcional, entrada2_opcional=5):
#def define a função 
#uma função é uma variavel 
# sempre escrver o 'def' e em seguida o nome da função
'''
Essa função...
'''
#
    return entrada1_opcional, entrada2_opcional

retornoFunção = (nomeFuncao(1,2))
print(retornoFunção[1])

retornoFunção = (nomeFuncao(([1,2],[1,2])),'a')
print(retornoFunção[0])

retornoFunção = (nomeFuncao([1,2],2))
print(retornoFunção[0])

retornoFunção = (nomeFuncao(entrada2_opcional=[1,2,3,4,5,6])
#print(retornoFunção[0])