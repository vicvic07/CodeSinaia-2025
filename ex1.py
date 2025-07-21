import matplotlib
import random

n=input ()
n=int(n)
mn=input ()
mn=int (mn)
mx=input ()
mx=int (mx)

v=[]
blud={}
mxval=0, mnval=1e18
for i in range (0, n):
    x=random.randint (mn, mx)
    if x not in blud:
        blud[x]=[]
    blud[x].append (i)
    v.append (x)
    mnval=min (mnval, x)
    mxval=max (mxval, x)
for i in v:
    print (i)
print (len (blud))
print (mxval)
print (mnval)


