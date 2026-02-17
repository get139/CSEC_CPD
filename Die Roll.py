import math


line = input().split()
y = int(line[0])
w = int(line[1])


max_roll = max(y, w)


successful_outcomes = 6 - max_roll + 1
total_outcomes = 6

common = math.gcd(successful_outcomes, total_outcomes)

numerator = successful_outcomes // common
denominator = total_outcomes // common

print(f"{numerator}/{denominator}")
