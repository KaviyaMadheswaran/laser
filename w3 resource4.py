Write a Python program to create a list reflecting the run-length encoding from a given list of integers or a given list of characters. Go to the editor
Original list:
[1, 1, 2, 3, 4, 4.3, 5, 1]
List reflecting the run-length encoding from the said list:
[[2, 1], [1, 2], [1, 3], [1, 4], [1, 4.3], [1, 5], [1, 1]]
l1=[1, 1, 2, 3, 4, 4.3, 5, 1]
l2=[-1]
l=l1+l2
c=0
ans=[]
for i in range(0,len(l)-1):
 if(c==1):
 i=k
 count=1
 consi=[]
 a=l[i]
 for j in range(i+1,len(l)):
 if(l[i]==l[j]):
 count+=1
 else:
 c=1
 consi.append(count)
 consi.append(a)
 ans.append(consi)
 k=j
 break
print(ans)
