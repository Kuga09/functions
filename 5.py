def f(a,b):
    if b == 0:
        print(a)
    else:
        c=a
        a=b
        b=c%b
        return f(a,b)
d=f(int(input()),int(input()))
