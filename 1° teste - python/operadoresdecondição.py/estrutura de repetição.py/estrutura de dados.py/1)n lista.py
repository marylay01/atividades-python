#programa que apresenta a menor a maior medida das temperaturas em graus celsius
a=[]
for i in range (10):
    a.append(float(input(f"digite a {i+1}o. temoeratura em graus celsius")))
a.sort()
print("a menor temperatura é",a[0])
print("a maior temperatura é",a[9])
print("a média das temperaturas é",sum(a)/10)
