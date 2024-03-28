#calcula o somatorio dos grãos de tfrigo de um tabuleiro de xadrez com while 
cont=1
soma=0
while cont<=64:
    soma+=(2**cont)-1
    print(soma)
    cont+=1
print("o total de grãos de trigo é de:",soma)