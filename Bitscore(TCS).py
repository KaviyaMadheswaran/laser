n=int(input())
l=list(map(int,input().split()))
bitscore=[]
for i in l:
  s=str(i)
  l1=[]
  for i in s:
    l1.append(int(i))
  maxi=max(l1)
  mini=min(l1)
  val=(maxi*11)+(mini*7)
  #len of that value
  st=str(val)
  if(len(st)==2):
    bitscore.append(int(st))
  else:
    bitscore.append(int(st[1:]))
uni=[]
for i in bitscore:
  if(i not in uni):
    uni.append(i)
print(len(uni)//2)
    
