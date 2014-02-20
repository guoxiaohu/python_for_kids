#!/bin/python
n = 21
for i in range(1, n):
	for j in range(1, n):
		if j <(n - 1) / 2 - i + 1:
	 		print(" "),
		elif j > (n - 1) / 2 + i - 1:
			print(" "),
		else:
			print("1"),
	print(" ")
