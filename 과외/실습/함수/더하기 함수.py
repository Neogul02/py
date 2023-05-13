def add_numbers(a, b): # 매개변수가 정해져 있을 경우
    return a + b

def add_many(*args): # 매개변수의 갯수가 정해져 있지 않을경우
    result = 0
    for i in args:
        result += i
    return result

print(add_numbers(3, 5))  # 8 출력
print(add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
