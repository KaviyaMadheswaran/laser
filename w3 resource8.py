Write a Python program to check whether all dictionaries in a list are empty or not. Go to the editor
Sample list : [{},{},{}]
Return value : True
Sample list : [{1,2},{},{}]
Return value : False
l=[{},{},{}]
#[{1,2},{},{}]...// False
c=0
for i in l:
 if(len(i)!=0):
 c+=1if(c==0):
 print(True)
else:
 print(False)
