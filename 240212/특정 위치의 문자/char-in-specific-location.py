word = ['L', 'E', 'B', 'R', 'O', 'S']
n = input()
idx= -1
for i in range(len(word)):
    if word[i] == n:
        idx = i

if idx == -1:
    print("None")
else:
    print(idx)