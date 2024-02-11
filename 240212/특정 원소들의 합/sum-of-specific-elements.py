lst = [list(map(int,input().split())) for i in range(4)]
summ = 0
for i in range(4):
    for j in range(4):
        if i >= j:
            summ += lst[i][j]

print(summ)