#!/usr/bin/env python

import fractions as f

max = 20
tiny = 1

for i in range(max, 1, -1):
    if (tiny % i != 0):
        print i, tiny, (tiny * i)#, math.gcd(tiny, i)
        tiny *= (i / f.gcd(tiny, i))
