import sys

def possible_vehicle(width_array,i,j):
	minimum=min(width_array[i:j+1])
	print minimum




list_of_lists = []
for line in sys.stdin:
    new_list = [int(elem) for elem in line.split()]
    list_of_lists.append(new_list)

n=list_of_lists[0][0]
testcases=list_of_lists[0][1]
width_array=list_of_lists[1]

for k in range(2,2+testcases):
	i=list_of_lists[k][0]
	j=list_of_lists[k][1]
	possible_vehicle(width_array,i,j)



