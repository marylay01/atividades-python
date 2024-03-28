resposta="sim"
while resposta=="sim":
    fatorial=1
    N=int(input("digite o valor"))
    for contador in range (1,N+1,1):
        fatorial*=contador
    print("o fatorial de",N,"é", fatorial)
    resposta=input("deseja calcular o fatorial de outro número? (sim/não)")
        
    