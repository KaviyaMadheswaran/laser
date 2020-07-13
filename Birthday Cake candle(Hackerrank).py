Output Format
  Return the number of candles that can be blown out on a new line.
Sample Input 0
  4
  3 2 1 3
Sample Output 0
  2
Explanation 0
  We have one candle of height 1, one candle of height 2, and two candles of height 3. Your niece only blows out the tallest candles, 
  meaning the candles where height = 3. Because there are 2 such candles, we print 2 on a new line.
n=int(input())
l=list(map(int,input().split()))
maxi=max(l)
c=0;
for i in l:
  if(i==maxi):
    c+=1
print(c)
