from datetime import date

def count_fridays(inp):
	counter=0
	d1,m1,y1,d2,m2,y2=int(inp[0]),int(inp[1]),int(inp[2]),int(inp[3]),int(inp[4]),int(inp[5])
	if d1>13:
		d1=1
		if m1==12:
			m1=1
			y1=y1+1
		else:
			m1=m1+1
	for y in range(y1,y2+1):
		if y != y1:m1=1
		tempm =  y == y2 and m2 or 12
		for m in range(m1,tempm+1):
			if date(y,m,13).weekday()==4:counter=counter+1
	print counter



testcases=input()
inp=[]

for i in range(1,testcases+1):
	val=raw_input()
	inp.append(val)

for x in inp:
	count_fridays(x.split())