

# N = int(input())
#
# res = 1
# for n in range(N, 0, -1):
#     res = res*n
# print(res)

def factorial(N):
    if N == 1:
        return 1
    elif N == 0 :
        return 1
    return N *factorial(N-1)

N = int(input())
print(factorial(N))