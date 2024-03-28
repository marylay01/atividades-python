# Programa que le valores e imprime o somatório, média e o total de valores. O programa para com valores negativos.
soma=0 
cont=1
while True:
    num=int(input("digite um número"))
    if num<0:
        break
    soma+=num
    media=soma/cont
    cont+=1
print("A soma desses vaores é:", soma)
print("A media desses valores é igual a:", media)
print("O total de valores lidos e:", cont-1)

    