#!/usr/bin/env python3

s = 0
sqs = 0

for i in range(101):
    s += i
    sqs += i*i
    print(i, s, i*i, sqs)

ssq = s*s
print(ssq, sqs, ssq-sqs)
