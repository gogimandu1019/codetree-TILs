n = int(input())
arr = input().split()
x = 0
answer = []
for i in range(n):
    x = 0
    x = int(arr[i]) **2
    answer.append(x)
    print(f'{answer[i]} ', end = "")