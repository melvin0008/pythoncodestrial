import sys
d={
        (1,1):[1],
        (1,2):[1,2],
        (1,3):[1],
        (1,4):[1,2],
        (2,1):[1,2],
        (2,2):[1,2],
        (2,3):[1,2,3],
        (2,4):[1,2],
        (3,1):[1],
        (3,2):[1,2,3],
        (3,3):[1,3],
        (3,4):[1,2,3,4],
        (4,1):[1,2],
        (4,2):[1,2],
        (4,3):[1,2,3,4],
        (4,4):[1,2,4]
}

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
  numlist= [int(n) for n in inp.split()]
  x=numlist[0]
  rc=(numlist[1],numlist[2])
  ans=d[rc]
  if x not in ans:
    return "RICHARD"
  else:
    return "GABRIEL"

if __name__ == '__main__':
    main(*sys.argv[1:])
