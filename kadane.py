def kadane():
	numarray=[4, -2, 7, 4, -8, -6, 2, 9, 1, 0, -4]

	currentmax=0
	currentstart=0
	maxnow=-999999
	for currentend in range (0,len(numarray)):
		currentmax=currentmax+numarray[currentend]
		if(currentmax>maxnow):
			maxnow,maxstart,maxend=currentmax,currentstart,currentend
			print currentmax
		if currentmax <=0:
			currentstart=currentend+1;
			currentmax=0;

	print "Max:"+str(maxnow)+"Start:"+str(maxstart)+"End:"+str(maxend)


kadane()
	 

