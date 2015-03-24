x,y,z,n=1 ,1,1,2
print [[o,p,q] for o in range(x+1)for p in range(y+1)for q in range(z+1)  if  (o+p+q)!= n ]
