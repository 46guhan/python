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
