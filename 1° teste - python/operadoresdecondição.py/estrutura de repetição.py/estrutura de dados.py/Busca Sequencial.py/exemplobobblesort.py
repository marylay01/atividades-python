# bublesort como funciona em python 
a=[5,4,3,2,1]
for i in range (len(a)-1):  #mesma coisa de colocar o 4
    for j in range(1+i,len(a)):
        if a[i]>a[j]:
            a[i], a[j] = a[j], a[i]
print(a)