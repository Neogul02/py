# 파이썬에서 input() 함수를 사용하여 사용자로부터 입력을 받을 수 있습니다. 
# input() 함수는 괄호 안에 사용자에게 보여줄 프롬프트를 넣으면 됩니다.

name = input("What is your name? ")  # 사용자로부터 이름을 입력받음
print("Hello, {}!".format(name))  # "Hello, 입력받은이름!" 출력

age_str = input("How old are you? ")  # 사용자로부터 나이를 문자열로 입력받음
age = int(age_str)  # 문자열을 정수로 변환
print("You will be {} years old next year.".format(age + 1))  # 입력받은 나이 + 1 출력