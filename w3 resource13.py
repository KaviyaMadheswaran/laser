INPUT FORMAT:first line contains x,k
second line contains quadratic equation of P
OUTPUT FORMAT:
if  P(x)==k...print True
 otherwise print False
INPUT:1
 4x**3 + x**2 + x +1
OUTPUT:True
EXPLANATION:P(1) = 1*1*1 +1*1 + 1+ 1 = 4 = k
hence the output is True
x,k=map(int,input().split())
s=input()
if(k==eval(s)):
    print(True)
else:
    print(False)
