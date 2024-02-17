A = input()
B = input()
strr = ""
cnt = 0

for i in range(0, len(A)-1, 1):
    strr = A[i]+A[i+1]
    if strr == B:
        cnt= cnt + 1

print(cnt)