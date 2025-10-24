T = int(input())
for _ in range(T):
    S = int(input())
    N = int(input())
    total=0
    for i in range(N):
        q, p = map(int, input().split())
        total += q * p
        
    print(total + S)