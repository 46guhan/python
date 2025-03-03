g=int(input("g="))
'print(type(g))'
if(g<10):
    print("g is lessthan 10")
elif(g==10):
    print("g is equal to 10")
else:
    print("g is greaterthan 10")

a=100
b=40
c=23
if(a>b)and(a>c):
    print("a is the greatest")
elif(b>a)and(b>c):
    print("b is the greatest")
else:
    print("c is the greatest")
'''
'''
name="gokul"
age=21
place="namakkal"
if(age>18 and place=="namakkal"):
    print("you are eligible to work")
else:
    print("you are not eligible")

x=int(input())
if x==1:
    print("odd numbers")
    for x in range(10):
        if x%2==0:
            continue
        print(x)
elif x==2:
    print("even numbers")
    for x in range(10):
        if x%2==0:
            print(x)
elif x==3:
    print("palindrome check")
    a=int(input())
    x=a
    b=0
    while(a>0):
        c=a%10
        b=(b*10)+c
        a//=10
    print(b)
    if x==b:
        print("palidrome")
    else:
        print("not palindrome")
elif x==4:
    print("")
    a=int(input())
    d=a
    b=0
    while(a>0):
        c=a%10
        b=b+(c**3)
        a//=10
    print(b)
    if d==b:
        print("true")
    else:
        print("false")
elif x==5:
    print("factorial")
    a=int(input())
    b=a-1
    while(a>0<b):
        c=a*b
        a=c
        b-=1
    print(c)
else:
    print("chose again")
