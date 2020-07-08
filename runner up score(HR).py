l=[]
n=int(input("enter number"))
for i in range(0,n): 
  element=int(input("enter inputs")) 
  l.append(element)
max=max(l[0],l[1])
sec_max=min(l[0],l[1])
for i in range(2,len(l)): 
  if(l[i]>max): 
    sec_max=max
    max=l[i] 
  else: 
    if(l[i]>min): 
      sec_max=l[i]
print(sec_max)
