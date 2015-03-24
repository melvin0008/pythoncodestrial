import sys

def got(y):
    d={x:y.count(x) for x in set(y)}
    flag=0
    print d
    for x in d.itervalues():
            print x
            if x %2!=0:
                	if flag==1:
                		return "NO"
                	else:
                		flag=1
    return "YES"

list_of_lists=[]

for line in sys.stdin:
    new_list = [int(elem) for elem in line.split()]
    list_of_lists.append(new_list)

print got(list_of_lists[0])
