a=[0,0,0,0,0,0,0,0,0,0]
A=int(input())
B=int(input())
C=int(input())
D=A*B*C
D=str(D)
for i in range(len(D)):
    a[int(D[i])]+=1
print('n'.join(map(str,a)))