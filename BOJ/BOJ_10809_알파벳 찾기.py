
# 값을 입력받고
# 입력된 문자열 안의 알파벳을 하나하나 훑으면서
# 알파벳 목록(이 있을 것이다)과 비교해서
# 문자열 내에 있으면 해당 위치(index) 출력
# 문자열 내에 없으면 -1 출력

sentence = input()
alphabet = list(range(97, 123))
for x in alphabet:
    print(sentence.find(chr(x)))



