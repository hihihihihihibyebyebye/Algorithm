N = int(input())
words = [input() for _ in range(N)]
for i in words:
    if i[::-1] in words:
        print(len(i), i[len(i)//2])
        break
