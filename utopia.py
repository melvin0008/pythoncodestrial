def current_height(ht,n):
	if n==0:
		return 1
	if n%2==0:
		ht=ht+1
	else:
		ht=2*ht
		
	return ht

def utopia(ht,start,index,val):
	if index>=len(val):
		return 
	else:
		for i in range(start,val[index]+1):
			ht=current_height(ht,i)
		index=index+1
		print ht
		return utopia(ht,start,index,val)



		#print str(i)+'->'+str(ht)
	#print ht
	



testcases=input()
inp=[]

for i in range(1,testcases+1):
	val=input()
	inp.append(val)

utopia(0,0,0,inp);





