Write a Python program to create a list reflecting the run-length encoding from a given list of integers or a given list of characters.
Original String:
automatically
List reflecting the run-length encoding from the said string:
[[1, 'a'], [1, 'u'], [1, 't'], [1, 'o'], [1, 'm'], [1, 'a'], [1, 't'], [1, 'i'], [1, 'c'], [1, 'a'], [2, 'l'], [1, 'y']]
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
 c=1
 ecount.append(c1)
 ecount.append(a)
 ans.append(ecount)
 k=j
 break
print(ans)


