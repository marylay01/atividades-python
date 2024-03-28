# ler elementos de uma lista e salvar como valores negativos em outra lista 
a=[]
b=[]
cont=0
while cont<5:
    n=int(input('digite um valor:'))
    if n>0:
        a.append(n)
        b.append(a[cont]* -1)
        cont+=1
    else:
        print('digite um valor positivo')

print(a)
print(b)
