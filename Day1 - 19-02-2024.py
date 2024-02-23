#P1 largest 0f 2
'''a=int(input())
b=int(input())
if a>b:
    print(a)
else:
    print(b)'''
#P2 largest of 3
'''
a=int(input())
b=int(input())
c=int(input())
if a>b and a>c:
    print(a)
elif b>c:
    print(b)
else:
    print(c)
    
'''
#P3 smallest of 2
'''
a=int(input())
b=int(input())
if a>b:
    print(b)
else:
    print(a)
    '''
#P4 2nd largest
'''
a=int(input())
b=int(input())
c=int(input())
if a>b and a>c:
    a=0
elif b>c:
    b=0
else:
    c=0
if a>b and a>c:
    print(a)
elif b>c:
    print(b)
else:
    print(c)'''
#P5 print many "Hello World"
'''
for i in range (1000):
    print("Hello World")
'''
#P6
'''
a,b=map(int,input().split())
if a>b:
    print("a > b")
elif  a<b:
    print("a < b")
else:
    print("a == b")
    '''
#P7 triangle valid or not
'''
a,b,c=map(int,input().split())
if a+b>c and b+c>a and a+c>b:
    print("Yes")
else:
    print("No")
    '''
#P8 Number reverse
#using str()
'''
n=int(input())
print(str(n)[::-1])
'''
#using while for +ive & -ve numbers
'''
n=int(input())
if n>0:
    rev=0
    while n>0:
        d=n%10
        rev=rev*10+d
        n=n//10
    print(rev)
elif n==0:
    print(n)
else:
    rev=0
    n=n*-1
    while n>0:
        d=n%10
        rev=rev*10+d
        n=n//10
    print(rev*-1)
   '''
#P9 watermelon
'''
w=int(input())
if w>2 and w%2==0:
    print("Yes")
else:
    print("No")
    '''
#P10 fever in foreign heat
#using while
'''
n=int(input())
while n>0:
    a=int(input())
    if(a>98):
        print("Yes")
    else:
        print("NO")
    n=n-1    
'''        
#using for
'''
n=int(input())
for i in range(n):
    a=int(input())
    if a>98:
        print("Yes")
    else:
        print("No")
        
'''
#P11 to find money paid based on discount
'''
n=int(input())
for i in range(n):
    a=int(input())
    print(100-a)
'''
#P12 discount
'''
n=int(input())
for i in range(n):
    a,b,c,d=map(int,input().split())
    if a-c>b-d:
        print("Second")
    elif a-c<b-d:
        print("First")
    else:
        print("any")
'''
#P13 n childern x candies
'''
t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    if n>x:
        k=n-x
        if(k%4==0):
            print(k//4)
        else:
            print(k//4+1)
    else:
        print(0)
'''
#P14 Pizza
#using for
'''
t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    k=n*x
    if(k%4==0):
        print(k//4)
    else:
        print(k//4+1)
        '''
#using while(called as brute force approach-->which is more efficient)
'''
t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    ts=n*x
    tp=0
    while ts>=4:
        tp=tp+1
        ts=ts-4
    if ts==0:
        print(tp)
    else:
        print(tp+1)
'''        
    

    
    

