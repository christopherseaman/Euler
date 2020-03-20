#!/usr/bin/env python3

prime = [2]
x = 3

while len(prime) < 10001:
    residue = x
    for i in range(len(prime)):
        while residue % prime[i] == 0:
            residue = residue / prime[i]
        if i < len(prime)-1:
#            if (x < prime[i+1] * prime[i+1]) | (residue % prime[i+1] != 0):
            if (residue < prime[i+1]) | (residue == 1):
                # print 'x:', x, '\tr:', residue, '\tp:', prime[i], '\tp+:', prime[i+1]
                break
    if residue != 1:
        prime.append(x)
    x += 1

print(prime)
print(prime[len(prime)-1])