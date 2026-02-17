n = int(input())
if not 1 <= n <= 1000:
    print("please enter between 1 up to 1000")
sum = 0

line = input().split()

P = int(line[0])
V = int(line[1])
T = int(line[2])


def input_repetition():
    global P, V, T
    line = input().split()
    P = int(line[0])
    V = int(line[1])
    T = int(line[2])


if (P, V, T == (0 or 1)):
    if P+V+T >= 2:
        sum += 1
    for i in range(n-1):
        input_repetition()
        if P+V+T >= 2:
            sum += 1
else:
    print("please enter the number either 1 or 0")
print(sum)
