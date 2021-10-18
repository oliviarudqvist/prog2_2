#!/usr/bin/env python3
from integer import Integer
from time import perf_counter as pc
import matplotlib.pyplot as plt
def fib_py(n):
	if n<=1:
		return n
	else:
		return(fib_py(n-1)+fib_py(n-2))
def main():
	f=Integer(5)
	print(f.get())
	f.set(7)
	print(f.get())
	n=47
	start_c=pc()
	f=Integer(n)
	fib47=f.fib()
	end_c=pc()
	print(fib47)
	print("time c++",end_c -start_c)
	start=pc()
	n=6
	fi=fib_py(n)
	end=pc()
	print(fi)
	print("time pyton",end-start)
	for i in range(30,45):
		start_cpp=pc()
		f=Integer(i)
		f.fib()
		end_cpp=pc()
		start_p = pc()
		fib_py(i)
		end_p=pc()
		plt.scatter(i,end_p-start_p, color='red')
		plt.scatter(i,end_cpp -start_cpp,color='blue')
	print("time  for loop of fib",end_cpp -start_cpp)
	plt.savefig("plotfibtime.png")
if __name__=='__main__':
	main()
