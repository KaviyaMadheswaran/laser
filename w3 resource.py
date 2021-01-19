Write a Python program to split a given list into two parts where the length of the first part of the list is given. Go to the editor
Original list:
[1, 1, 2, 3, 4, 4, 5, 1]
Length of the first part of the list: 3
Splited the said list into two parts:
([1, 1, 2], [3, 4, 4, 5, 1])
n=int(input())
l=list(map(int,input().split()))
ans=[]
l1=l[:n]
l2=l[n:]
ans.append(l1)
ans.append(l2)
print(tuple(ans))
