# programa que le 10 valores e apresente a soma desses valores e as medidas deles  
soma=0
cont=1
while cont<=10:
    valor=int(input("digite o valor:"))
    soma+=valor 
    cont+=1
media=soma/10
print("A soma desses vaores é:", soma)
print("A media desses valores é igual a:", media)