# programa que une duas listas em uma outra
a=[]
b=[]
c=[]
for i in range (5):
    a.append(int(input("digite o nÚmeoro para  a lista A:")))
    b.append(int(input("digite o nÚmeoro para  a lista B:")))
c=a+b
print(c)