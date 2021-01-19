Write a Python program to decode a run-length encoded given list. Go to the editor
Original encoded list:
[[2, 1], 2, 3, [2, 4], 5, 1]
Decode a run-length encoded said list:
[1, 1, 2, 3, 4, 4, 5, 1]
l=[[2, 1], 2, 3, [2, 4], 5, 1]
ans=[]
for i in l:
 if(isinstance(i,list)):
 #first element in i means count of second element
 a=i[0] 
#element in secon position
 b=i[-1]
 for j in range(a):
 ans.append(b)
 else:
 ans.append(i)
print(ans)
