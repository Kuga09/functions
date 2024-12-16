k=0
def contains(S,n):
    if len(S) != 0:
        if S[0]!=n:
            S.remove(S[0])
            return contains(S,n)
        else:
            return True
    else:
        return False
print()
S=list(input())
print()
n=input()
answer=contains(S,n)
print(answer)