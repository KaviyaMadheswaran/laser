#python basic 
>>> a=10
>>> a
10
>>> b=a+4
>>> b
14
>>> a=a+4
>>> a
14
>>> a=10
>>> a
10
>>> b=a+4
>>> b
14
>>> a=a+4
>>> a
14
>>> a=20
>>> a
20
>>> b=a+4
>>> b
24
>>> a=a+4
>>> a
24
>>> id(b)
1401674272
>>> id(a)
1401674272
>>> b=12
>>> id(b)
1401674080
>>> #multiple variable single value
>>> a=b=c=d=5
>>> a
5
>>> print(b)
5
>>> print(a,b,c,d)
5 5 5 5
>>> print(a,b,c,d,sep=',')
5,5,5,5
>>> print(a,b,c,d,sep=',',end='.')
5,5,5,5.
>>> 
