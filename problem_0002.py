#!/usr/bin/env python3


a = 1
b = 1
s = 1
sum = 0

while b < 4000000:
    print('%d\t%d' % (b, sum))
    s = a + b
    a = b
    b = s
    if b % 2 == 0:
        sum += b

print(sum)
