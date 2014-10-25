def almost_sorted(inp,current,total,counter):

	if(current==total):
		return counter

	if(inp[current]<inp[current+1]):

		return almost_sorted(inp,current+1,stop,total,counter+1)
	else:
		return almost_sorted(inp,current+1,stop+1,total,counter+1)








list_of_lists = [3,1,2,5,4]
"""for line in sys.stdin:
    new_list = [int(elem) for elem in line.split()]
    list_of_lists.append(new_list)

total=list_of_lists[0][0]
"""
total=5
val=almost_sorted(list_of_lists,0,0,total,0)


