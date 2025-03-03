##basic programs

#factorial of a num
'''
a=int(input("enter the number:"))
i=a
b=a-1
while(b>0):
    c=a*b
    a=c
    b-=1
print("the fibonecci of ",int(i),"=",c)
'''

#find simple intrest
'''
p=int(input("principal="))
t=int(input("time="))
r=int(input("intrest rate="))

si=(p*t*r)/100
print("simple interst=",si)

#find compound interest

amount=p*(1+(r/100))**t
ci=amount-p
print("compound interst=",ci)
'''

#check amstrong number
'''
a=int(input("enter the num:"))
b=0
while(a>0):
    c=a%10
    b=(c**3)+b
    a//=10
print(b)
'''
#find area of circle
'''
import math
r=int(input("radious="))
pi=math.pi

a=pi*(pow(r,2))
b=pi*(r**2)
print("area of circle=",a,b)
'''
#print prime num in range

x=[]
for i in range(2):
    x.append(int(input('enter the numbers:')))
    m=max(x)
    for a in x:
        while(a<m):
            a+=1
            print(a)
        

    

    

