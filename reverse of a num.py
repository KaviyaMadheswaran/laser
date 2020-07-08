n=int(input("enter num"))
reverse=0
while(n>0):
   rem=n%10
   reverse=(reverse*10)+rem
   n=n//10
print(reverse)
