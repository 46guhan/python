'''
print("hello","world")
print("hello"+"world"+"python")
print("wellcome","to","data","science",sep="*")
print("thank",end="")
print("you")
'''
'''
g=int(input("g="))
'print(type(g))'
if(g<10):
    print("g is lessthan 10")
elif(g==10):
    print("g is equal to 10")
else:
    print("g is greaterthan 10")'''
'''
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

age+=5
print(age)
'''
'''
for x in range(5):
    print(x)
for x in range(1,5):
    print(x)
for x in range(1,5):
    if x==3:
        break
    print(x)
for x in range(1,6):
    if x==3:
        continue
    print(x)
for x in range(15):
    if x%2==0:
        continue
    print(x)
'''
'''

a="some char"
for x in a:
    if x=="a" or x=="e" or x=="i" or x=="o" or x=="u":
        continue
    print(x)
'''
'''
a=123
c=0
while(a>0):
    r=a%10
    c=(c*10)+r
    a//=10
print(c)
'''
'''
a=12
b=0
c=a**2
while(c>0):
    d=c%10
    b=(b*10)+d
    c//=10
e=12
f=0
while(e>0):
    g=e%10
    f=(f*10)+g
    e//=10
h=f**2
print(b,h)
if(b==h):
    print("this is adem number")
else:
    print("not adem number")
'''
'''
a=153
e=a
b=0
while(a>0):
    c=a%10
    b=(c**3)+b
    a//=10
print(b,e)
if(e==b):
    print("true")
else:
    print("false")
'''
'''
a=0
b=a+1
while(a<8):
    c=a+b
    a=b
    b=c
    print(c)
'''
'''
q=5
w=q-1
while(q>0<w):
    e=q*w
    q=e
    w-=1
print(e)
'''
'''
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
 '''
'''
def squar(a):
    return(a**2)

def rev(a):
    b=0
    while(a>0):
        c=a%10
        b=(b*10)+c
        a//=10
    return(b)

if squar(rev(12))==rev(squar(12)):
    print("true")
else:
    print("fase")
 '''
'''
def ams(a):
    b=a+1
    while(a<10):
        c=a+b
        a=b
        b=c
        print(c)
ams(0)
'''
'''
fruits1=['apple','banana','orenge']
fruits2=['mango','graps']

fruits1.append('mango')
print(fruits1)

fruits1.extend(fruits2)
print(fruits1)

fruits1.pop()
print(fruits1)

fruits1.insert(2,'mango')
print(fruits1)

fruits1.remove('orenge')
print(fruits1)

fruits1.sort()
print(fruits1)

print(fruits1.index('mango'))

print(fruits1.index('mango',3))

print(fruits1.count('mango'))

fruits2=fruits1.copy()
fruits2.pop()
print(fruits1)
print(fruits2)
'''
'''
name=[]
age=[]
id=[]
degree=[]

for x in range(5):
    name.append(input("name: "))
    age.append(int(input("age:")))
    id.append(int(input("id:")))
    degree.append(input("degree:"))

print(name,age,id,degree,sep="\n")
'''
'''
a={'ant','bird','cat','dog'}
b={'rat','bug','lion'}

a.add('snake')
print(a)
a.remove('bird')
print(a)
a.pop()
print(a)
print(a|b)
print(a&b)
print(a^b)
'''
'''
name={'k7'}
age={'20'}
degree={'bsc'}
percentage={'70'}
for i in range(3):
    name.add(input("name="))
    age.add(int(input("age=")))
    degree.add(input("degree="))
    percentage.add(input("percentage="))
print(name,age,degree,percentage,sep="\n")
'''
'''
elec=['mobile','laptop','tv',]
non_elec=['cart','table','cycle']
mobile=['samsung','vivo','oppo','apple']
laptop=['samsumg','lenovo','apple','rog']
tv=['lg','sony','redmi','samsung']
cart=['steel','light wood','havy wood']
table=['square','round',]
cycle=['sport','lady','child']
print("1-electronics","2-non electrinics",sep="\n")
x=int(input("your choice:"))
if x==1:
    print(elec)
    print("1-mobile","2-laptop","3-tv",sep="\n")
    a=int(input("your choise:"))
    if a==1:
        print(mobile)
    elif a==2:
        print(laptop)
    elif a==3:
        print(tv)
    else:
        print("chose again")
elif x==2:
    print(non_elec)
    print("1-cart","2-table","3-cycle",sep="\n")
    b=int(input("your choise:"))
    if b==1:
        print(cart)
    elif b==2:
        print(table)
    elif b==3:
        print(cycle)
    else:
        print("chose again")
else:
    print("chose again")
'''
'''
elec=['mobile','laptop','tv',]
non_elec=['cart','table','cycle']
print("1-electronics","2-non electrinics",sep="\n")
x=int(input("your choice:"))
if x==1:
    print(elec)
    print("1-mobile","2-laptop","3-tv",sep="\n")
    a=int(input("your choise:"))
    if a==1:
        print("mobile is Rs15000")
    elif a==2:
        print("laptop is Rs50000")
    elif a==3:
        print("tv is Rs25000")
    else:
        print("chose again")
elif x==2:
    print(non_elec)
    print("1-cart","2-table","3-cycle",sep="\n")
    b=int(input("your choise:"))
    if b==1:
        print("cart is Rs20000")
    elif b==2:
        print("table is Rs10000")
    elif b==3:
        print("cycle is Rs8000")
    else:
        print("chose again")
else:
    print("chose again")
'''
'''
def v_remove(a):
    b=['a','e','i','o','u']
    for x in a:
        if x in b:
            continue
        print(x)
v_remove("happiest")
'''
'''
dic={'name':'ram','age':26}
dic['class']=12
del dic['age']
print(dic)

for item in dic:
    print(item)

for value in dic.values():
    print(value)


for item,value in dic.items():
    print(item, value)
'''
'''
a={}
name=[]
age=[]
clas=[]

for x in range(3):
    name.append(input("name: "))
    age.append(int(input("age:")))
    clas.append(input("degree:"))

a['name']=name
a['age']=age
a['class']=clas
print(a)
for item,value in a.items():
    print(item, value)
'''
'''
a=input()
v=['a','e','i','o','u']
count=0
for x in a:
    if x in v:
        count+=1
print(count)
'''
'''
q=input()
b=q.split()
b.sort()
c=" ".join(b)
print(c)
'''
'''
import math
from circle import circle_area
print(circle_area())
'''
'''
from circle import circle_area
from circle import circle_c

print(circle_area(20))
print(circle_c(25))
'''
'''
from ud_modules import ams
from ud_modules import v_remove
from ud_modules import reverse_num
from ud_modules import fibonacci
from ud_modules import adem_num
from ud_modules import num_153

print(ams(5))
print(v_remove("data science"))
print(reverse_num(2307))
print(fibonacci(4))
print(adem_num(12))
print(num_153(153))
'''
'''
import numpy as np

a=np.array([1,2,3,4,5,6,7,8])
for i in a:
    print(i)

b=np.array([[[1,2,3,4,5],[6,7,8,9,10]],[[11,12,13,14,15],[16,17,18,19,20]]])

for x in b:
    for y in x:
        for z in y:
            print(z)


x=0
while (x<len(b)):
    a=b[x]
    y=0
    while(y<len(a)):
        c=a[y]
        z=0
        while(z<len(c)):
            print(c[z])
            z+=1
        y+=1
    x+=1
'''
'''
a=[]
for x in range(5):
    a.append(int(input()))
print(max(a))
print(sum(a))
'''
'''
a=[1,2,3,4,5]
def rev(count):
    while(count>0):
        count-=1
        a.append(a[0])
        a.remove(a[0])
    print(a)
rev(int(input("times of reverse:")))
'''
'''
a=[1,2,3,4,5,7]
l=int(input())
s=a[l-1]
b=a[:s]
c=a[s:]
for x in b:
    c.append(x)
print(c)
'''
'''
import matplotlib.pyplot as plt
import numpy as np
a=[]
b=[]
for i in range(3):
    a.append(int(input("x elements:")))
    b.append(int(input("y elements:")))
print(a)
print(b)
print("markers","1.o","2.+","3.*",sep="\n")
m=int(input("marker is:"))
if m==1:
    m="o"
elif m==2:
    m="+"
elif m==3:
    m="*"
else:
    print("invalid choise")
print("line design","1.:","2._",sep="\n")
l=int(input("line:"))
if l==1:
    l=":"
elif l==2:
    l="_"
else:
    print("invalid choise")
print("colors","1.green","2.white","3.black","4.yellow")
c=int(input("chose color:"))
if c==1:
    c="g"
elif c==2:
    c="w"
elif c==3:
    c="k"
elif c==4:
    c="y"
else:
    print("invalid choise")
'data=m+l+c'
x=np.array(a)
y=np.array(b)
plt.plot(x,y, m+l+c)
plt.show()
'''
'''
import matplotlib.pyplot as plt
import numpy as np
a1=np.array([23,20,12,17])
a2=np.array([0,18,23,21])
plt.plot(a1,a2, marker="*", ms="20", mfc='k', linewidth="4")
font1={'family':'serif','color':'blue','size':'15'}
font2={'family':'serif','color':'green','size':'15'}
plt.title("graph",size=20)
plt.xlabel("a1",fontdict=font1)
plt.ylabel("a2",fontdict=font2)
plt.show()
'''
