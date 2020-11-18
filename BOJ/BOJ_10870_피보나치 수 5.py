

def Fibbo(n):
    if n<=1:
        return n
    return Fibbo(n-1) + Fibbo(n-2)

n = int(input())
print(Fibbo(n))