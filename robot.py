def robot(inp):
	d=[(0,-1),(1,0),(0,1),(-1,0)]
	multiple= inp/4
	x,y=(-multiple)*2,(-multiple)*2
	mod=inp%4
	# if mod>0:
	for i in xrange(1,mod+1):
		x,y=x+(multiple*4+i)*(d[i][0]),y+(multiple*4+i)*(d[i][1])
	print x,y

testcases=input()
inp=[]

for i in xrange(1,testcases+1):
	val=raw_input()
	inp.append(val)

for x in inp:
	robot(int(x))
