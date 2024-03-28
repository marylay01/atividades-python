# programa que imprime a soma dos numeros IMPARES de uma lista de 5 numeros 
a=[]
soma=0
for i in range (0,5):
    a.append(int(input(f"digite um numero:")))    #o f é uma formatação para conseguir colocar uma variavel dentro do print 
    if a[i]%2!=0:
        soma+=a[i]
print("a soma dos numeros impares é:",soma)