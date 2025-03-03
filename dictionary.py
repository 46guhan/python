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
