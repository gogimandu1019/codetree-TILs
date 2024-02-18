A = input()
B = input()

x = len(A)
cnt = 0

for i in range(x):
    A = A[1:] + A[0]
    cnt += 1

    if A == B:
        print(cnt)
        break;