summ=0
def sum_digits(n,summ):
    if n !=0:
        summ+=n%10
        return sum_digits(n//10,summ)
    else: 
        return summ
summ=sum_digits(int(input()),summ)
print(summ)