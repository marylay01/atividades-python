# apresentar os resultados de uma tabuada de um número qualquer 
n=int(input("digite um numero para ver a tabuada "))  #já que o número ai ser o que eu colocar, tem que ter uma variável para isso 
print("Tabuada da multiplicação de um número",n)      #só para dizer que o que vem abaixo é a tabuada da variavel de cima 
c=1  #padrão 
while c <= 10: 
    print(n, "x", c, "=", n*c)   #estrutura da tabuada 
    c+=1
continua=input("deseja continuar (sim/não)")
if continua=="não":
    breakpoint