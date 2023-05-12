num = int(input("숫자를 입력하세요: "))

if num < 2:
    print("소수가 아닙니다.")
else:
    for i in range(2, num):
        if num % i == 0:
            print("소수가 아닙니다.")
            break
    else:
        print("소수입니다.")
