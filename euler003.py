#!/usr/bin/env python3

composite = 600851475143
#sqrt = sqrt(600851475143)
i = 2

while (i < composite):
    if (composite % i == 0):
        print(i)
        composite = composite / i
        i = 2
    i += 1

print(composite)
