a=int(input("digite um numero"))  #efetuar o cálculo da equação completa de segundo grau, utilizando a formula de Baskara
b=int(input("digite um número"))
c=int(input("digite um número"))
delta= (b**2)-4*a*c  #começo da fórmula(valor pra delta)
bas1p= (-b+(delta**0.5))/2*a  #fórmulas de bahskara para menos e mais 
bas2n= (-b-(delta**0.5))/2*a  #a raíz de delta esta representada como 
if a!=0 and b!=0 and c!=0: #condição para a equação ter raizes, as variaveis precisam ser maior que 0.
    if delta==0: #primeira condição de como as raizes vão sair se delta for  que igual 0
        print("x1 e x2 são iguais", bas1p, bas2n) #sem aspas significa o valor numérico
    if delta>0:
        print("x1 e x2 são diferentes", bas1p, bas2n)    
    if delta<0:
        print("nao existem raizes reais")