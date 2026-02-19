n = int(input())
if not 1 <= n <= 100000:
    print("you have to enter between 1 and 100,000")
group = 0
lastMagnet = ""
for _ in range(n):
    currentMagnet = input()
    if currentMagnet != lastMagnet:
        group += 1
        lastMagnet =currentMagnet
print(group)
