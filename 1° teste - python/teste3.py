#calculo do inss
vh=float (input("digite o valor ganho por hora:"))
ht= float(input("digite as horas trabalhadas:"))
print(f"o seu salario liquido é de: {(vh*ht) - ((vh*ht ) * 14/100)}")