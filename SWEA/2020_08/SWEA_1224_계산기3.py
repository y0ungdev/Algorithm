
import sys
sys.stdin = open("input.txt", "r")


def calc_postfix(express):
    # 입력값들을 연산할 때 숫자들을 보관할 리스트 생성
    global res
    stack_res = []
    for data in express:
    # 만약 입력값의 형태가 정수라면 그대로 리스트에 넣기
        if type(data) is int:
            stack_res.append(data)
            continue

        elif data == '+' :
            num1 = stack_res.pop()
            num2 = stack_res.pop()
            res = stack_res.append(num1 + num2)
        # elif data == '-' :
        #     num1 = stack_res.pop()
        #     num2 = stack_res.pop()
        #     res = stack_res.append(num1 - num2)
        elif data == '*':
            num1 = stack_res.pop()
            num2 = stack_res.pop()
            res = stack_res.append(num1 * num2)
        # elif data == '/' :
        #     num1 = stack_res.pop()
        #     num2 = stack_res.pop()
        #     res = stack_res.append(num1 // num2)

    return res


tc_len = int(input())

for tc in range(1, tc_len+1):
    print('#{} {}'.format(tc, calc_postfix(express)))
