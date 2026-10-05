#Write a Python program to generate the first N terms of the Fibonacci series using iteration.
#
#Input: N = 10
#
#Output: 0 1 1 2 3 5 8 13 21 34
n=int(input("enter the number:"))

a=0
b=1

for i in range(n):
	print(a)
	a, b = b, a + b
