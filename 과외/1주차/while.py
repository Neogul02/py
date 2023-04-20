# 파이썬에서 while문은 조건문이 참(True)일 동안 
# 반복적으로 코드를 실행합니다. 다음은 while문의 기본 구조입니다.

# while 조건문:
#     실행할 코드1
#     실행할 코드2
#     ...

i = 0
while i < 5:
    print(i)
    i += 1

# 짝수인 경우에는
while i < 10:
    if i == 5:
        break
    if i % 2 == 0:
        i += 1
        continue
    print(i)
    i += 1