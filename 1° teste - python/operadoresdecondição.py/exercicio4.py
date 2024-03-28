a=int(input("primeiro lado do triangulo"))
b=int(input("digite um número"))
c=int(input("digite um número"))
if a<b+c and b<a+c and c<a+b:
    if a==b==c:
        print("triangulo equilatero")
    elif a==b or a==c or b==c:
        print("triangulo isóceles")
    else:
        print("triangulo escaleno")
else: 
    print("os lados nao formam nenhum triangulo") 