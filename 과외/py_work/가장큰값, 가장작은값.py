# 채점을 원하기 하기 위하여 정답 부분은 빨강색 처리 요망

number_1 = int(input("첫번째 정수를 입력하시오:"))
number_2 = int(input("두번째 정수를 입력하시오:"))
number_3 = int(input("세번째 정수를 입력하시오:"))
 
# 가장 큰값 찾기
if number_1 >= number_2:
    if number_1 > number_3:
        max_number = number_1
    else:
        max_number = number_3
else:
    if number_2 > number_3:
        max_number = number_2
    else:
        max_number = number_3


# 가장 작은값 찾기

if number_1 < number_2:

    if number_1 < number_3:

        min_number = number_1

    else:

        min_number = number_3

else:

    if number_2 < number_3:

        min_number = number_2

    else:

        min_number = number_3 


print("가장 큰값 :", max_number, "가장 작은값", min_number)
