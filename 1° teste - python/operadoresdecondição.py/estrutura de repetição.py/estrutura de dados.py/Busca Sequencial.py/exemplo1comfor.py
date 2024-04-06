lista=[1,2,3,4,5,6,7,8,9,10]
resp="sim"

while True:
    achou=False #inicializando como falso 
    n=int(input("digite um número para buscar na lista:")) 
    cont=0
    while cont<len(lista): #len lista é para ler quantos elementos tem na lista que ja foi definida 
        if lista [cont]==n:
            achou=True
            break
        cont+=1        
    if achou:
        print("o numero",n,"foi encontrado na posição",cont+1)   
        
    else:
        print("o numero",n,"não encontrado na posição")
    resp=input("deseja buscar por outro numero?")
    if resp=="não":
        break
print("fim do programa")