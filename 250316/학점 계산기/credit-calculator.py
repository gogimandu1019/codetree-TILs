N = int(input())
score = list(map(float, input().split()))

x = len(score)
avg = 0
summ = 0
result = ""

for i in range(x):
    summ += score[i]

avg = round(summ / x, 1)

if avg >= 4.0:
    result = "Perfect"
elif avg >= 3.0:
    result = "Good"
else:
    result = "Poor"

print(avg)
print(result)