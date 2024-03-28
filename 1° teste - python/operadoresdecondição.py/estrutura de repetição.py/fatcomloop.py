#programa que calcula o fatorial de um nuemro que o usuario digita usando while true 
while True:
    fatorial=1
    n=int(input("digite o valor"))
    for contador in range (1,n+1,1):
        fatorial*=contador
    print("o fatorial de",n,"é", fatorial)
    continuar=input("deseja calcular o fatorial de outro número? (sim/não)")
    if continuar =="não":
        break 
        