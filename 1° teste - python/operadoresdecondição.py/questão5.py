a=int(input("digite o valor"))  #4 vlores que o programa diz se vai ser divisivel por 2 e por 3 ao msm tempo 
b=int(input("digite o valor"))
c=int(input("digite o valor"))
d=int(input("digite o valor"))
#para o resto ser 0 
if a%2==0 and a%3==0: 
    print(a)      #pq a diviãso precisa ter resto 0 para que a divisão seja exta, divisivel pelos dois numeros  
if b%2==0 and b%3==0: 
    print(b)      #então eu coloco a condiçao de que as variaveis divididas por 2 ou 3 tem que dar resto 0
if c%2==0 and c%3==0: 
    print(c)         #apenas os numeros que aparecerem depois de executar serão divisiveis por 2 e 3, dentre os valores que eu colocar como variavel
if d%2==0 and d%3==0: 
    print(d)