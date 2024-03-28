# ler elementos de uma lista A para uma lista B, seguindo a seguinte lei de criação 
# se o indice de A for par multiplica a 5 e se for impar soma por 5

a=[]
b=[]
for i in range (1,6):
    a.append(int(input(f"digite o {i}° numero:")))    #o f é uma formatação para conseguir colocar uma variavel dentro do print 
    if (i-1)%2==0:
        b.append(a[i-1]*5) 
    else:
        b.append(a[i-1]+5)
       
print(a)
print(b)