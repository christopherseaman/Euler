#!/usr/bin/env python3

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

composite = 600851475143

i = 2

while (i < composite):
    if (composite % i == 0):
        # i is a factor, show it to me
        print(i)
        # remove i from the composite number
        composite = composite / i
        # reset to smallest possible i
        # note: I've done this inefficiently
        i = 2
    i += 1

print(composite)
