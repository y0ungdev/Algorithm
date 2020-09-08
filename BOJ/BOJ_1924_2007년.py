

x, y = map(int, input().split())

# 2007.01.01 월요일
# 일주일을 기점으로 요일이 반복된다는 것 이용

month_31 = [1,3,5,7,8,10,12]
month_30 = [4,6,9,11]
month_28 = 2

sumDays = 0

for i in range(x):
    if i in month_31 :
        sumDays += 31
    elif i in month_30:
        sumDays += 30
    else:
        sumDays += 28
sumDays += y
if sumDays % 7 == 1:
    print('MON')
elif sumDays % 7 == 2:
    print('TUE')
elif sumDays % 7 == 3:
    print('WED')
elif sumDays % 7 == 4:
    print('THU')
elif sumDays % 7 == 5:
    print('FRI')
elif sumDays % 7 == 6:
    print('SAT')
elif sumDays % 7 ==0 :
    print('SUN')