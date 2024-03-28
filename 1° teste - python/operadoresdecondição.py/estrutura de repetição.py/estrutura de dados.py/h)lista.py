# ler valores inteiros em uma lista "a" e colocar em ordem decrescente numa lista "b"
a=[]
b=[]
for i in range (5):
    a.append(int(input("digite o nÚmeoro para  a lista A:")))
for j in range (-1, -6, -1):        #o -1 é o ultimo numero da lista 
    b.append(a[j])

print("lista A:", a)
print("lista B:", b)


