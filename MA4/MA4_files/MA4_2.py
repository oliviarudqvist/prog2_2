#!/usr/bin/env python3

from integer import Integer

def main():
	f = Integer(5)
	print(f.get())
	f.set(7)
	print(f.get())
	#f = Integer(n)
	#f.fib()
	n=5
	fi = fib_py(n)
	print(fi)
def fib_py(n):
	if n<= 1:
		return n
	else:
		return(fib_py(n-1)+fib_py(n-2)


if __name__ == '__main__':
	main()
