list=[1,2,2,3,3,4,4]
count=0
for i in range(len(list)-1):
   if(list[i]==list[i+1]):
      count=count+1
print(count)

