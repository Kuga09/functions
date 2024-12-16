def IsPalindrom(S):
    if len(S)<=1:
        return True
    elif S[0] == S[-1]:
        return IsPalindrom(S[1:-1])
    else:
        return False
answer=IsPalindrom(input())
print(answer)