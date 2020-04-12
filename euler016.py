#!/usr/env python3

# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26. 
# What is the sum of the digits of the number 2^1000?
import pandas

digits = str(2**1000)

print(digits, len(digits))

sum =0
for i in range(len(digits)):
	sum += int(digits[i])
	
print(sum)
