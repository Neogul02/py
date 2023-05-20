# 파이썬 함수의 구조
# def 함수명(매개변수):
#   <수행할 문장 1>
#   <수행할 문장 2>
#   return 리턴 값


def sum(a, b):  # 일반적인 함수
    return a + b


def say():  # 입력 값이 없는 함수
    return "Hi"


def add(a, b):  # 리턴 값이 없는 함수
    print("%d + %d = %d" % (a, b, a + b))


def say2():  # 입력 값도 리턴 값도 없는 함수
    print("Hi")


def add_many(*args):  # 여러개의 입력값을 받는 함수
    result = 0
    for i in args:
        result += i
    return result


# 함수의 리턴값은 언제나 하나.
