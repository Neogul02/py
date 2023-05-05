# 구구단 만들기

number = int(input('구구단 몇 단을 출력할까요? : '))

for i in range(10):
    print(number, "x", i, "=", number*i)