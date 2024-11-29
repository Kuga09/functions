user_input=input()
opertation='Error'
list_operations=['+','-','*','/','^']
for i in user_input: 
    for h in list_operations:
        if i == h:
            opertation=h
            number_list=user_input.split(h)
            break

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
    case _:
        print(opertation)