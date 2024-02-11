n = int(input())
arr = list(map(int, input().split()))
answer = []
cha = 0

for i in range(n):
    for j in range(i+1 , n):
        cha = arr[j] - arr[i]
        answer.append(cha)


print(min(answer))