

# 알파벳으로 이루어진 문자열을 입력 받아 각 알파벳을 1부터 26까지의 숫자로 변환하여 출력하라.

T = int(input())

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for t in range(T):
    date = input()
    mon = int(date[4:6])
    day = int(date[6:8])
    if 1<= mon <= 12 and 1<= day <= days[mon - 1]:
        result = date[0:4] + "/" + date[4:6] + "/" + date[6:8]
        print (f'#{t+1} {result}')
    else:
        print (f'#{t+1} -1')   
    
