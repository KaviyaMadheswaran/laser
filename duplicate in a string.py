s="kaviya"
s1="kiruthika"
l=[]
l1=[]
for i in s: 
  l.append(i)
for i in s1: 
  l1.append(i)
s=""
if(len(l)<len(l1)): 
  for i in range(0,len(l)): 
    if(l[i] in l1):
       ind=l1.index(l[i])
       l1.pop(ind)
       s+=l[i]
print(s)
