Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. Go to the editor
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2
s=input()
l=s.split(" ")
c=0
for i in range(0,len(l)):
 a=l[i]
 if(len(a)>=2 and a[0]==a[-1]):
 c+=1
print(c)
