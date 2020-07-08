n=int(input("enter number?"))
c=0
t=n
while(n>0):
   a=n%10
   c=c+(a*a*a)
   n=n//10
if(t==c):
    print("armstrong number")
else:
   print("not an armstrong number")
