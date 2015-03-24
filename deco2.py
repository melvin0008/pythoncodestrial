import sys
from operator import itemgetter

def sortbyname(func):
    def wrapper(innerlist):
        return func(['Mr. '+x[0]+' '+x[1] if x[3]=='M' else 'Ms. '+x[0]+' '+x[1] for x in innerlist])
    return wrapper

@sortbyname
def printnames(namelist):
    for name in namelist:
        print name


list_of_lists=[]

for line in sys.stdin:
    new_list = [elem for elem in line.split()]
    list_of_lists.append(new_list)

innerlist=list_of_lists[1:]
innerlist.sort(key=itemgetter(2))

printnames(innerlist)
