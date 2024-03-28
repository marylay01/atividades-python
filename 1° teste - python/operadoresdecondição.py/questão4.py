a=int(input("digite um numero"))   #questao sobre os valores em ordem crescente, reorganizando 
b=int(input("digite um número"))    #Ler três valores e apresenta-los em ordem crescentee, onceitos de propriedade distributiva e troca de valores entre variáveis.
c=int(input("digite um número"))
if a>b:        #todas as combinações possiveis
    a,b=b,a              #esses são os valores atribuídos a cada uma das condiçoes que na hora de atribuir ficam em a,b,c por padrão
if b>c:
    b,c=c,b
if a>b:
    a,b=b,a
print(a, b, c ) 