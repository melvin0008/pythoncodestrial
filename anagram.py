def anagram(inp):

	for i in range(0,len(inp)):
		flag=0
		counter=0
		string=inp[i]
		visited=[]
		l=len(string)
		if(l%2==0):
			string1=string[:l/2]
			string2=string[l/2:]
			
			for i in range(0,l/2):
				ch=string1[i]
				if ch not in visited:
					first=string1.count(ch)
					second=string2.count(ch)
					if first==second:
						visited.append(ch)
						continue
					elif first>second:
						flag=1
						counter=counter+first-second
						visited.append(ch)
					
			if(flag!=1):
				print '0'
			else:
				print counter
		else:
			print '-1'

testcases=input()
inp=[]

for i in range(1,testcases+1):
	val=raw_input()
	inp.append(val)

anagram(inp)
