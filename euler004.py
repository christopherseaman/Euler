#!/usr/bin/env python3
import math

m = 0

for i in range(100, 1000):
    for j in range(i, 1000):
        s = str(i * j)
        for x in range(len(s)):
            if (s[x] != s[len(s) - x - 1]):
                break
            if x == (len(s) -1):
                print(s, s[x], s[len(s) - x - 1], x, i, j)
                if int(s) > m:
                    m = int(s)
print(m)
