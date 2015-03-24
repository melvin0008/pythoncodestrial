def gem(inp):
	mainstr=inp[0]
	visited=[]
	counter=0

	for i in range(0,len(mainstr)):
		ch=mainstr[i]
		incounter=0
		if ch not in visited:
			for j in range(1,len(inp)):
				present=inp[j].find(ch)
				if(present!=-1):
					incounter=incounter+1

				else:
					visited.append(ch)
					break
				
				if(incounter==len(inp)-1):
					counter=counter+1
				visited.append(ch)

	print counter		




testcases=input()
inp=[]

for i in range(1,testcases+1):
	val=raw_input()
	inp.append(val)

gem(inp)
