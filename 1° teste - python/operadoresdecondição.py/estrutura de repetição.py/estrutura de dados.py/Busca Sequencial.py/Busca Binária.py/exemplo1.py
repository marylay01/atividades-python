# inicio+fim /2 (0+11/2 == 5,5 mas apenas nos interessa a lista inteira ou seja o  meio vai ser ==5)
# fim = meio - 1
# inicio == fim - não encontrei o que estou buscando
a=[91,81,77,22,21,14,10,8,7,4]
for i in range (len(a)-1):  #primeiramente ordenar com buble sort
    for j in range(1+i,len(a)):
        if a[i]>a[j]:
            a[i], a[j] = a[j], a[i]
print(a)
inicio=0
fim=len(a)-1
meio=(inicio+fim)//2
x=100
while inicio<=fim and a[meio] !=x:
    if x<a[meio]:
        fim=meio-1
    else:
        inicio=meio+1
    meio=(inicio+fim)//2
if a[meio]==x:
    pirnt("elemento encontrado na posição",meio)
else:
    print("ele")


