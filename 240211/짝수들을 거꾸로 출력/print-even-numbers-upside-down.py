n = int(input())
arr =  input().split()

for i in range(n-1, -1, -1):
    if int(arr[i]) % 2 == 0:
        print(int(arr[i]), end = " ")