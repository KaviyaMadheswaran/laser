Write a Python program to create a list by concatenating a given list which range goes from 1 to n. Go to the editor
Sample list : ['p', 'q']
n =5
Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']  
l=["p","q"]
n=5
s=[]
for i in range(1,n+1):
    for j in l:
        s1=""
        s1+=j
        s1+=str(i)
        s.append(s1)
print(s)
        
    
