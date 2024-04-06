# programa que busca um elemento em uma lista 
lista=[1,2,3,4,5,6,7,8,9,10]
resp="sim"
while True:
    n=int(input("digite um número para buscar na lista:")) 
    if n in lista:
        print("o numero",n,"esta na lista")
    else:
        print("o numero",n,"não esta na lista")
    resp=input("deseja buscar por outro numero?")
    if resp=="não":
        break
print("fim do programa")