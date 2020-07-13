Input Format
  A single line of five space-separated integers.
Output Format
  Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. 
  (The output can be greater than a 32 bit integer.)
Sample Input
1 2 3 4 5
Sample Output
10 14
EXPLANATION:
  1.If we sum everything except 1, our sum is  2+3+4+5 = 14.
  2.If we sum everything except 2, our sum is  1+3+4+5 = 13.
  3.If we sum everything except 3, our sum is  1+2+4+5 = 12.
  4.If we sum everything except 4, our sum is  1+2+3+5 = 11.
  5.If we sum everything except 5, our sum is  1+2+3+4 = 10.
print minimum of above sum value and maximum of above sum value.
l=list(map(int,input().split()))
sumval=[]
for i in range(0,len(l)):
  a=l[:i]+l[i+1:]
  sumval.append(sum(a))
s=""
s+=str(min(sumval))+" "+str(max(sumval))
print(s)

