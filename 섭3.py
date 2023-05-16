import random

print("[간단한 산술연산 연습 프로그램]")
test_num = int(input("연습할 문제수: "))
test_case = input("(수의크기) 1. 단자리(0~9) 2. 두자리(10~99) 3. (세자리(100~999): ")

print("<<< 시작합니다 >>>")
answer_cnt = 0
for i in range(test_num):
    if test_case == "1":
        a = random.randrange(1, 10)
        b = random.randrange(1, 10)
        print("[문제 %d] %d+%d = " % (i + 1, a, b), end="")
        user_num = int(input())

        if user_num == a + b:
            print("==> 맞았습니다.")
            answer_cnt += 1
        else:
            print("==> 틀렸습니다.")

    elif test_case == "2":
        a = random.randrange(10, 100)
        b = random.randrange(10, 100)
        print("[문제 %d] %d+%d = " % (i + 1, a, b), end="")
        user_num = int(input())
        if user_num == a + b:
            print("==> 맞았습니다.")
            answer_cnt += 1
        else:
            print("==> 틀렸습니다.")

    elif test_case == "3":
        a = random.randrange(100, 1000)
        b = random.randrange(100, 1000)
        print("[문제 %d] %d+%d = " % (i + 1, a, b), end="")
        user_num = int(input())
        if user_num == a + b:
            print("==> 맞았습니다.")
            answer_cnt += 1
        else:
            print("==> 틀렸습니다.")
print("<<< 결과 >>>")
print(
    "총 %d문제 중에서 %d문제를 맞췄습니다.(정답율 %.1f%%)"
    % (test_num, answer_cnt, (answer_cnt * 100) / test_num)
)
