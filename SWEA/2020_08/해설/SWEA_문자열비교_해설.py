

# Brute Force 이용

def check(str1, str2):
    # 본문에서 패턴 길이를 빼고 +1 하여 반복 => index 범위 때문에
    for i in range(len(str2)-len(str1)+1) :
        # 패턴의 길이만큼
        for j in range(len(str1)):
            # 만약 현재 사이클과 다르다면 브레이크
            if str2[i+j] != str[j]:
                break
        # 중간에 브레이크 X => 다 찾은 것
        else:
            return 1
    # 완벽히 찾지 못했다면 return 0
    return 0


T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    print("#{} {}".format(tc, check(str1, str2)))

     ans = 0
    if str2.find(str1) != -1 :
        ans = 1
    print("#{} {}".format(tc, ans))