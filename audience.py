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

def run_case(it):
  inp=it.next()
  index=inp.find(' ')
  smax, audlevel=inp[:index],inp[index+1:]
  standing=[]
  friends=0
  if smax==0:
    return 0
  for inx, val in enumerate(audlevel):
    standing.append(int(val))
    sumval=sum(standing)
    if sumval<(1+inx):
      friends=friends+1
      standing.append(1)
  return friends

if __name__ == '__main__':
    main(*sys.argv[1:])



