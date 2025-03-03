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

def v_remove(a):
    b=['a','e','i','o','u']
    for x in a:
        if x in b:
            continue
        print(x)
v_remove("happiest")
