#programa que recebe numeros pares para lista a e numeros impares para lista b, e junta as listas 
a,b,c=[],[],[]
#atribuindo elementos a lista a 
cont=0
while cont<6:
    n=(int(input("digite um numero par:")))
    if n%2==0:
        a.append(n)
        cont+=1
    else:
        print("Número impar ")
# atribuindo os valores à lista b
print("inserindo elementos da lista a")
cont=0
while cont<6:
     n=(int(input("digite um numero impar:")))
     if n%2!=0:
        b.append(n)
        cont+=1
     else:
        print("numero par")
c=a+b 
    
print(c)