Questions MarksHave the function QuestionsMarks(str) take the str string parameter,
 which will contain single digit numbers, letters, and question marks, and check
 if there are exactly 3 question marks between every pair of two numbers that add up to 10.
 If so, then your program should return the string true, otherwise it should return the string false.
 If there aren't any two numbers that add up to 10 in the string, then your program should return false as well.
For example: if str is "arrb6???4xxbl5???eee5" then your program should return true
 because there are exactly 3 question marks between 6 and 4, and 3 question marks between 5 and 5 at the end of the string.
ExamplesInput: "aa6?9"
Output: false
Input: "acc?7??sss?3rr1??????5"
Output: true
def QuestionsMarks(str):
  # code goes here
  s=str
  dig=[]
  ind=[]
  if("?" not in s):
    ans="false"
  else:
    for i in range(0,len(s)):
      if(s[i].isdigit()):
        dig.append(s[i])
        ind.append(i)
  yes=0
#for check the count .. if "?" is present in between all pairs
  ov=0
#if "?" is present in between pairs then their countshould >= 3
  ov1=0
  for i in range(0,len(ind)-1):
    a=ind[i]
    b=ind[i+1]
    su=int(s[a])+int(s[b])
    l=s[a+1:b]
    if("?" in l):
      ov+=1
    c=0
    for i in l:
      if(i=="?"):
        c+=1
    if(c>=3):
      ov1+=1
    if(c>=3 and su==10):
      yes+=1
  if(yes>=1 and ov==ov1):
    ans="true"
  else:
    ans="false"
  return ans
# keep this function call here
 print(QuestionsMarks(input()))
