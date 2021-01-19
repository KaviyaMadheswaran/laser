Ex 20)
1:special string reverse
Input Format:
b@rd
output Format:
d@rb
Explanation:

We should reverse the alphabets of the string by

keeping the special characters in the same position
s=input()
alp=[]
#index of char
ind=[]
for i in range(0,len(s)):
 if(s[i].isalpha()):
 alp.append(s[i])
 else:
 ind.append(i)
rev=alp[::-1]
for i in ind:
 #character value in s 
char=s[i]
 rev.insert(i,char)
print(rev)


