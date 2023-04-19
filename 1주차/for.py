# 파이썬에서 for문은 반복문의 한 종류로, 
# 시퀀스(리스트, 튜플, 문자열 등)나 이터레이터를 순회하면서 
# 각 요소에 대한 작업을 반복적으로 수행할 때 사용됩니다.

# for 변수 in 시퀀스:
#     실행할 코드1
#     실행할 코드2
#     ...

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


for i in range(5):
    print(i)

#  for문에서 break와 continue 키워드를 사용하여 반복문의 실행을 제어할 수 있습니다. 
# break는 반복문을 중지하고 continue는 해당 반복을 건너뛰고 다음 반복으로 넘어갑니다.