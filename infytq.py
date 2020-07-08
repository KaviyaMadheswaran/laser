s=input()
l=[]
for i in s.split(','): 
  l.append(i)
  a=input()
  b=input()
a1=l.index(a)
b1=l.index(b)
ans=[]
if(a in l and b in l): 
  if(a1>b1): 
    ans=l[b1:a1+1] 
    for j in ans: 
      s="" 
      s+=j 
      n1=int(j)
l2=[]
for i in l: 
  if(i not in ans): 
    l2.append(int(i)) 
    n2=sum(l2)
print(n1+n2)
