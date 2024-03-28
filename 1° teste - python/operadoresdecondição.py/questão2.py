a=float(input("digite a nota")) #calcular a média para saber se o aluno foi aprovado u reprovado 
b=float(input("digite a nota"))
c=float(input("digite a nota"))
d=float(input("digite a nota"))
ma=(a+b+c+d)/4 
if ma>=7:
    print("aprovado", ma)
else:                        #se foi reprovado, mostrar a nota do exame final 
    print("reprovado", ma)
    e=float(input("digite a nota"))  # variavel para o exame final 
    media=(ma+e)/2  #depois somar com a media (ou seja, fazer a media de todas as notas)
    if media>=5:      #se for maior que 5 cinco aprovado, menor reprovado
        print("aprovado em exame final", media)
    else: 
        print("reprovado", media)