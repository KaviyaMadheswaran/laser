Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples. Go to the editor
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
l= [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
#laste element in each tuplelastelement=[]
#last elements index position
lastindex=[]
for i in range(0,len(l)):
 a=l[i]
 lastelement.append(a[-1])
 lastindex.append(i)
#sorted lastelements
ort=sorted(lastelement)
#index value for sorted tuple
finalind=[]
for i in sort:
 finalind.append(lastelement.index(i))
ans=[]
for i in finalind:
 ans.append(l[i])
print(ans)



 
