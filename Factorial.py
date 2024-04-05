def fact(n):
	'''
	returns factorial of n
	note use of recursion
	'''
	#BASE CASE
	if n <= 0:
		return 1
	#Recursion
	else:
		return n * fact(n - 1)