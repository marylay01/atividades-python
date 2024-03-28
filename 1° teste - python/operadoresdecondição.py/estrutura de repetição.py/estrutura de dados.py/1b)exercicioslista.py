# letra b lista de estrutura de dados
# ler 8 elementos de uma matriz a e criar uma outra matriz c
a=[]
b=[]
for i in range (0,8):
    a.append(int(input(f"digite o {i+1} elemento de número A:")))
    b.append(a[i]*3)
print(f"o vetor B é:{b}")