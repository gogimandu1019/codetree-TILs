arr = list(map(int, input().split()))
n = len(arr)
arr2 = []
for i in range(n):
    if arr[i] == 0:
        break;
    arr2.append(arr[i])

for j in arr2[::-1]:
    print(j, end = " ")