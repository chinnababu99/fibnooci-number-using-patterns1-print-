l=[]
def fib(n):
    if n==1 or n==2:
        return n-1
    return fib(n-1) +fib (n-2)
num=11
for a in range (1,num+1):
    if a>=3:
        l.append(fib(a))

l1=[]
l2=[]
for a in range (len(l)):
    if a%2==0:
        l1+=[l[a]]
    else:
        l2+=[l[a]]
st1=1
sp1=0
for a in range (len(l1)):
    for b in range(sp1):
        print(' ',end=' ')
    for c in range (st1):
        print(l1[a],end=' ')
    print()
    sp1+=2
sp2=6
st2=1
for x in range (-1,-(len(l2)+1),-1):
    for y in range(sp2):
        print(' ',end=' ')
    for z in range (st2):
        print(l2[x],end=' ')
    print()
    sp2-=2
    
    
