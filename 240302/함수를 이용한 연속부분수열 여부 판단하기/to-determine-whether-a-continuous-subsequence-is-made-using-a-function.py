n1, n2 = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


for i in range(n1):
    if A[i] == B[0]:
        for j in range(1, n2):
            if A[i] == B[j]:
                i += 1
                print("Yes")
                continue;
            else:
                print("No")
                break;

    else:
        if i < n1:
            i += 1
            continue;