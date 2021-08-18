def max_frobenius(a, b, c, d):
	n = {n for x in range(0, 101, a) for y in range(x, 101, b) for n in range(y, 101,c) for z in range(n, 101, d)}
	g = {n for n in range(101)}
	print("Max Frobenius:", max(g.difference(n)))

def n_nuggets(n, validPacks, howmany) :
	for i in range(len(validPacks)):
		curpack = validPacks[i]
		if(n - curpack) >= 0:
			retval = n_nuggets(n-curpack, validPacks, howmany)
			howmany[i] += 1
			if retval is True:
				return retval
			else:
				howmany[i] -= 1
		if n == 0:
			return True
	return False

n = 50

howmany = [0, 0, 0, 0]
max_frobenius(4,6,9,20)
validPacks = [20, 9, 6, 4]

print(n, ":", n_nuggets(n, validPacks, howmany), howmany)
