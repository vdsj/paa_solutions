import matplotlib.pyplot as plt
import time

count = 1
_max = 40
time_max = 0

x = list()
y = list()

def fibonacci(n):
	if n <= 1:
		return n
	else:
		return fibonacci(n - 1) + fibonacci(n - 2)

while count < _max and time_max <= 60.0:
	inic = time.time()
	seq_fib = fibonacci(count)
	end = time.time()
	time_current = end - inic

	print(f'{count} {time_current:.6f}')
	x.append(count)
	y.append(time_current)
	count += 1
	time_max += time_current

plt.plot(x, y)
plt.xlabel('Valores de n')
plt.ylabel('Tempo (s)')
plt.xticks(range(1, 40, 2))
plt.show()
