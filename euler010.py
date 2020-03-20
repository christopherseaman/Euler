#!/usr/bin/env python3

import gmpy2 as g

prime = [2]
sum = 0

while prime[len(prime)-1] < 2000000:
    sum += prime[len(prime)-1]
    prime.append(g.next_prime(prime[len(prime)-1]))
prime.pop(len(prime)-1)
print(prime[len(prime)-1], sum)
