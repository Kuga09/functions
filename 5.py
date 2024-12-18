def GCD(a,b):
    if b == 0:
        print(a)
    else:
        c=a
        a=b
        b=c%b
        return GCD(a,b)
inpt=input()
inpt=inpt.split()
a=int(inpt[0])
b=int(inpt[1])
print(a)
print(b)
d=GCD(a,b)
