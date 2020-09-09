

import sys
sys.stdin = open("input.txt", "r")


priority = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}

for tc in range(1, 11):
    input()
    line = input()
    ans = ''
    stack = []

    for i in range(len(line)):
        # 괄호라면
        if line[i] == '(' or line[i] == ')' :
            if line[i] == '(':
                stack.append(line[i])

            else:
                # 여는 괄호가 나올 때까지 pop
                while stack[-1] != '(' :
                    ans += stack.pop()
                # 여는 괄호 하나 버리기
                stack.pop()
        # isdigit()은 내장함수
        elif line[i].isdigit():
            ans += line[i]
        # 연산자일 때
        else :
            if len(stack) == 0:
                stack.append(line[i])
            else :
                # 연산자 우선순위를 비교 분석
                while priority[stack[-1]] >= priority[line[i]]:
                    ans += stack.pop()
                    if len(stack) == 0:
                        break
                stack.append(line[i])
    # 남아있는 스택 비우기
    while len(stack) > 0:
        ans += stack.pop()

            ######################### 중위 -> 후위
    for i in ans :
        if i.isdigit():
            stack.append(int(i))
        else:
            B = stack.pop()
            A = stack.pop()
            if i == '+' :
                stack.append(A+B)
            elif i == '-' :
                stack.append(A-B)
            elif i == '*':
                stack.append(A*B)
            elif i == '/' :
                stack.append(A/B)

    print('#{} {}'.format(tc, stack.pop()))