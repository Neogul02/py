# 채점을 원할히 하기 위하여 정답 부분은 빨강색 처리 요망

count = 1
number = []                            # 정수를 담아둘 리스트 변수 초기화
 
while True:                             # 정수를 number리스트에 순서대로 저장한다.
    print("%d번째 정수를 입력하시오: "%count, end="")
    no = input()
    if no == "":                         # 숫자 입력없이 <Enter>키를 누르면 입력 종료
        break
    else:
        count += 1
        number.append(int(no))
 
max_number = -999
min_number = 999
 
for no in number :  # for문 부터 아래 가장 큰값과 작은값을 찾는 코드를 작성할 것

    if max_number < no :

        max_number = no

    if min_number>no :

            min_number = no

print("가장 큰값 :", max_number, "가장 작은값 :", min_number)
# print(“가장 큰값 : %d  가장 작은값 : %d”%(max_number, min_number)) 
