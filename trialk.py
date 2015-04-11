from math import ceil
t=input()
for i in range(1,t+1):
    d=input()
    ds=map(int,raw_input().split())
    ckk = max(ds)
    answer = 999999
    for ra in range(1,ckk+1):
        curans=0
        for skt in ds:
            curans += int(ceil(skt/float(ra)))-1
        curans+=ra
        answer=min(answer,curans)
    print "Case #"+str(i)+": "+str(answer)
