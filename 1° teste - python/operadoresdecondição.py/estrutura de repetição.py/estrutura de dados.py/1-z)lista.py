# programa que conta a quantidade de elementos impares de uma lista e calcula  o percentual de elementos 
a=[]
impar=0
total=0
for i in range (10):
    a.append(int(input("digite um numero:")))
    if a[i]%2!=0:
        impar+=1
    total+=1
print("a quantodade de elementos impares é:", impar)
print("O percentual de elementos impares é:", (impar/total)*100,"%")
