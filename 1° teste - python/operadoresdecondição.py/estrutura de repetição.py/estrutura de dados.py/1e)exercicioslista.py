a=[]
b=[]
for i in range (5):
     a.append(int(input(f"digite um valor para a lista A:")))
     fatorial=1
     for j in range (1,a[i]+1):
         fatorial=fatorial*j
     b.append(fatorial)
print("lista A:", a)
print("lista B:", b)