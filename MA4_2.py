#!/usr/bin/env python3

from integer import Integer
from time import perf_counter as pc
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def fib_py(n):
	if n <= 1:
		return n
	else:
		return(fib_py(n-1) + fib_py(n-2))





def main():

	for n in range(30,46):

		start = pc()
		print(fib_py(n))
		end = pc()

		print(f"Python took {round(end-start, 2)} seconds for n = {n}")

		plt.plot(n, round(end-start, 2), 'r.')



		start2 = pc()
		f = Integer(n)
		f = f.fib()
		print(f)
		end2 = pc()

		print(f"C++ took {round(end2-start2, 2)} seconds for n = {n}")

		plt.plot(n, round(end2-start2, 2), 'b.')
	plt.savefig(f'FibTimes.png')

	f = Integer(47)
	print(f.fib())

if __name__ == '__main__':
	main()
