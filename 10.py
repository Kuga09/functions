n=''
def revers_number(S,n):
    if len(S)!=0:
        n = n + S[-1]
        return revers_number(S[:-1],n)
    else:
        return n
answer=revers_number(input(),n)
print(answer)
"""def revers_number(S, n=''):
    if len(S) != 0:
        n = n + S[-1]
        return revers_number(S[:-1], n)
    else:
        return n
answer = revers_number(input())
print(answer)"""
