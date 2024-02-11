a, b = map(int, input().split())
answer = [0] * 10
left = 0
x = 0
while (a > 1):
    left = a % b
    answer[left] += 1
    a = a // b


for i in range(10):
    if answer[i] != 0:
        x = x + answer[i] **2

print(x)