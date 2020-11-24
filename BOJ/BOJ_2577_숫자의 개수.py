

A = int(input())
B = int(input())
C = int(input())

res = int(A)*int(B)*int(C)
res = str(res)

for i in range(0, 10):
    print(res.count(str(i)))