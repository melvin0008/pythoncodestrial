def fact (acc,n):
	if n==0:
		return acc
	else:
		return fact(acc*n,n-1)


print fact(1,998)



