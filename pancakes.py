import math

import sys

def main(*args):
    lines = [line.strip() for line in sys.stdin]
    it = iter(lines)
    num_cases = int(it.next())
    for case_no in range(num_cases):
        try:
            output = run_case(it)
            if type(output) == list or type(output) == tuple :
                output = ' '.join(output)
            print("Case #%d: %s" % (case_no + 1, output))
        except StopIteration, e:
            print("Error: Input exhausted.")

def pancakes(pan,maximum,iteration):
	c=pan.count(maximum)
	if float(maximum)/float(2)<=iteration+1 or int(c>=maximum/2) :
		return iteration+maximum
	for index,x in enumerate(pan):
		if x==maximum:
			temp1,temp2=(x/2,x/2) if x % 2 ==0 else( (x+1)/2,x/2)
			pan[index]=temp1
			pan.append(temp2)
			iteration=iteration+1
			if float(maximum)/float(2)<=iteration+1:
				break
			# print pan
	# print pan
	return pancakes(pan,max(pan),iteration)

def run_case(it):
  it.next()
  inp=it.next()
  pan= [int(n) for n in inp.split()]
  return pancakes(pan,max(pan),0)


# b=[2,9,9,9,3]
# print pancakes(b,max(b),0)
if __name__ == '__main__':
	main(*sys.argv[1:])
