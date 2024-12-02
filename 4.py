user_input=input()
opertation='Error'
list_operations=['+','-','*','/','^','!']
for i in list_operations: 
    if i in user_input:
        number_list=user_input.split(i)
        opertation=i

def add():
    result=float(number_list[0])
    for g in range(1,len(number_list)):
        result+=float(number_list[g])
    print(result)

def subtract():
    result=float(number_list[0])
    for g in range(1,len(number_list)):
        result-=float(number_list[g])
    print(result)

def multiply():
    result=float(number_list[0])
    for g in range(1,len(number_list)):
        result*=float(number_list[g])
    print(result)

def devide():
    result=float(number_list[0])
    for g in range(1,len(number_list)):
        result/=float(number_list[g])
    print(result)

def power():
    result=float(number_list[0])
    power_full=float(number_list[1])
    for g in range(2,len(number_list)):
      power_full*=float(number_list[g])
    result=result**power_full
    print(result)

def factorial():
    result=1
    for g in range(2,int(number_list[0])+1):
        result=result*g
    print(result)

match opertation:
    case '+':
        add()
    case '-':
        subtract()
    case '*':
        multiply()
    case '/':
        devide()
    case '^':
        power()
    case '!':
        factorial()
    case _:
        print(opertation)