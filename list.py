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
