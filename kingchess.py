

class Chessboard:
        chessboard={}
        possibleoptions=[]
        kings={}
        def __init__(self):
                for i in range(1,11):
                        for j in range(1,11):
                                self.chessboard[(i,j)]=0

                self.chessboard[(4,4)]=2
                self.chessboard[(7,4)]=2
                self.chessboard[(2,2)]=1
                self.chessboard[(2,3)]=1
                self.chessboard[(2,4)]=1
                self.chessboard[(2,5)]=1
                self.chessboard[(5,1)]=1
                self.chessboard[(5,5)]=1
                self.chessboard[(1,5)]=1
                self.chessboard[(6,1)]=1
                self.chessboard[(6,5)]=1
                self.chessboard[(9,2)]=1
                self.chessboard[(9,3)]=1
                self.chessboard[(9,4)]=1
                self.chessboard[(9,5)]=1
                self.chessboard[(10,5)]=1

                self.chessboard[(4,7)]=2
                self.chessboard[(7,7)]=2
                self.chessboard[(2,6)]=1
                self.chessboard[(2,7)]=1
                self.chessboard[(2,8)]=1
                self.chessboard[(2,9)]=1
                self.chessboard[(5,6)]=1
                self.chessboard[(5,10)]=1
                self.chessboard[(1,6)]=1
                self.chessboard[(6,6)]=1
                self.chessboard[(6,10)]=1
                self.chessboard[(9,6)]=1
                self.chessboard[(9,7)]=1
                self.chessboard[(9,8)]=1
                self.chessboard[(9,9)]=1
                self.chessboard[(10,6)]=1
                self.kings[(4,4)]=0
                self.kings[(7,4)]=0
                self.kings[(4,7)]=0
                self.kings[(7,7)]=0
                
        def check(self,i,j):
                val=self.checkvalue(i,j)
                if val==0 or val==1:
                        newi,newj,val1=self.checkforking(i,j)
                        if(newi,newj==i,j):
                                self.chessboard[(i,j)]=2
                        self.kingstrikes(newi,newj)
                elif val==2:
                        self.kingstrikes(i,j)
                        newi,newj=i,j
                self.evalauteoptions(newi,newj)
                i,j,mini=self.chooseone()
                if mini ==3:
                        print len(self.kings)-4
                        return 0
                self.chessboard[(i,j)]=2
               
                if (i,j) not in self.kings:
                        self.kings[(i,j)]=0
                             
                        print "kings->",i,j,"\n"
                       
                else:
                        val=self.kings[(i,j)]
                        val=val+1
                        self.kings[(i,j)]=val
                self.check(i,j)

        def chooseone(self):
                mini=999
                if self.possibleoptions:
                        i=self.possibleoptions[0][0]
                        j=self.possibleoptions[0][1]
                        
                else:
                        
                        for key, value in self.kings.iteritems():
                                if self.kings[key]< mini:
                                        mini=self.kings[key]
                                        tup=key
                        i,j=tup[0],tup[1]
                return i,j,mini
                
        def checkvalue(self,i,j):
                return self.chessboard[(i,j)]

        def checkforking(self,i,j):
               
                for k in range(-1,2):
                        for l in range(-1,2):
                                if((i+k)<1)or((j+l)<1):
                                        continue
                                if((i+k)>10)or((j+l)>10):
                                        continue
         
                                if((self.checkvalue(i+k,j+l)==2)):
                                        return i+k,j+l,1
                return i,j,0

        def kingstrikes(self,i,j):
                for k in range(-1,2):
                        for l in range(-1,2):
                               self.chessboard[i+k,j+l]=1
        def display(self):
                for i in range(1,11):
                        print "\n"
                        for j in range(1,11):
                                print chessboard[(i,j)]

        def evalauteoptions(self,i,j):
                del self.possibleoptions[:]
                for l in range(-2,3):
                        for m in range(-2,3):
                            if l!=-2 and l!=2:
                                if m!=-2 and m!=2:
                                    continue
                            if((i+l)<1)or((j+m)<1):
                                continue
                            if((i+l)>10)or((j+m)>10):
                                continue
                            if(self.chessboard[(i+l,j+m)]==1) or (self.chessboard[(i+l,j+m)]==2):
                                continue
                            in1,in2,retval=self.checkforking(i+l,j+m)
                            if retval==1:
                                    continue
                            tup=(i+l,j+m)
                            self.possibleoptions.append(tup)
                            
                            
        
cb=Chessboard()
cb.check(4,7)

#in1,in2,retval=checkforking(6,4)
#print retval
#display()
