
tel = input()
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

res = 0
for i in range(len(tel)):
    for j in dial:
        if tel[i] in j :
            res += dial.index(j)+3
print(res)