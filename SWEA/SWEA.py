

# 10개의 수를 입력 받아, 그 중에서 가장 큰 수를 출력하는 프로그램을 작성하라.

n = int(input())

numbers = list(map(int, input().split()))
numbers.sort()
print(numbers[int(n//2)])
