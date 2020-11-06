

num1,num2 = list(map(str, input().split()))

num11 = int(num1[::-1])
num21 = int(num2[::-1])

if num11 > num21:
    print(num11)
elif num11 < num21 :
    print(num21)


