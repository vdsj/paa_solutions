import math

def exp_num(a, n):
	if n == 1:
	  return a

	if n % 2 == 0: 
		value = exp_num(a, math.floor(n/2)) * exp_num(a, math.floor(n/2))
	else: 
		value = exp_num(a, math.floor(n/2)) * exp_num(a, math.ceil(n/2))

	return value

print(exp_num(1, 10000))
print(exp_num(2, 10))
print(exp_num(3, 5))
