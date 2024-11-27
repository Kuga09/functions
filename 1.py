s=input()
a=list(s)

if len(s)!=3:
    a.remove(s[2])
    a.remove(s[4])
opertation=s[2]

def add(a,b):
    result=int(a)+int(b)
    print(result)

def subtract(a,b):
    result=int(a)-int(b)
    print(result)

def multyply(a,b):
    result=int(a)*int(b)
    print(result)

def devide(a,b):
    result=int(a)/int(b)
    print(result)

match opertation:
    case '+':
        add(s[1],s[3])
    case '-':
        subtract(s[1],s[3])
    case '*':
        multyply(s[1],s[3])
    case '/':
        devide(s[1],s[3])

