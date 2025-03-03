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


a="some char"
for x in a:
    if x=="a" or x=="e" or x=="i" or x=="o" or x=="u":
        continue
    print(x)
