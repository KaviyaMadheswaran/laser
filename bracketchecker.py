s=input()
ol=['[','{','(']
cl=[']','}',')']
#close brackets 
clo=[]
#close brackets range
clrange=[]
#open brackets
l=[]
#open brackets range
oprange=[]
for i in s:
  if(i in ol):
    l.append(i)
    oprange.append(s.index(i))
  else:
    pos=cl.index(i)
    if(len(l)>=1 and l[-1]==ol[pos]):
      l.pop()
      oprange.pop()
    else:
      clo.append(i)
      clrange.append(s.index(i))
if(len(l)==0 and len(clo)==0):
  print("Balanced")
else:
  print("Not balanced")
