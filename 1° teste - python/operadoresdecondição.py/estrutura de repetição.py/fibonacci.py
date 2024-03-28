primeiro =1   #serie de fibonacci
segundo=1 
print(primeiro)
print(segundo)
cont=2
while cont <15:
    proximo=primeiro +segundo
    print(proximo)
    primeiro= segundo
    segundo=proximo
    cont+=1
    for cont in range (1,14):
        proximo = primeiro+segundo 
        print(proximo)
        primeiro= segundo
        segundo=proximo
print("fim da serie de Fibonacci")