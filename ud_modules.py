def ams(a):
    b=a+1
    while(a<10):
        c=a+b
        a=b
        b=c
        return(c)

def v_remove(a):
    b=['a','e','i','o','u']
    for x in a:
        if x in b:
            continue
        return(x)

def reverse_num(a):
    c=0
    while(a>0):
        r=a%10
        c=(c*10)+r
        a//=10
    return(c)

def fibonacci(q):
    w=q-1
    while(q>0<w):
        e=q*w
        q=e
        w-=1
    return(e)

def adem_num(a):
    e=a
    b=0
    c=a**2
    while(c>0):
        d=c%10
        b=(b*10)+d
        c//=10
    f=0
    while(e>0):
        g=e%10
        f=(f*10)+g
        e//=10
    h=f**2
    print(b,h)
    if(b==h):
        return("this is adem number")
    else:
        return("not adem number")

def num_153(a):
    e=a
    b=0
    while(a>0):
        c=a%10
        b=(c**3)+b
        a//=10
    print(b,e)
    if(e==b):
        return("true")
    else:
        return("false")
