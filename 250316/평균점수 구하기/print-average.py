score = list(map(float, input().split()))

n = len(score)
avg = 0
summ = 0
for i in range(n):
    summ += score[i]

avg = round(summ / n, 1)
print(avg)