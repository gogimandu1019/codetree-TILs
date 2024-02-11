n = int(input())
arr = list(map (int, input().split()))

answer = [0]*10

for i in arr:
    answer[i] += 1

for j in range(1, 10):
    print(answer[j])