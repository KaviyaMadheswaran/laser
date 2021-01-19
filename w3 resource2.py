s1=input()
s=s1+"#"
c=0
ans=[]
for i in range(0,len(s)-1):
 if(c==1):
 i=k
 c1=1
 #elementcount
 ecount=[]
 a=s[i]
 for j in range(i+1,len(s)):
 if(s[i]==s[j]):
 c1+=1
 else:
#here is the condition used ...
if.count greater than 1 means append both count and the string 
else append string alone....this conditions depend upon the output asked..above 
if(c1>1):
 c=1
 ecount.append(c1)
 ecount.append(a)
 ans.append(ecount)
 k=j
 break
 elif(c1==1):
 c=1
 ans.append(a)
 k=j
 break
print(ans)


