#!/usr/bin/env python3

from math import factorial

f = str(factorial(100))

sum = 0

for i in range(len(f)):
    sum += int(f[i])

print(sum)
