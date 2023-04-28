#메뉴함수 프로그램 14주차
def choice_menu():
    print("0.종료")
    print("1.합계점수")
    print("2.평균점수")
    print("3.최고점수")
    print("4.최저점수")
    print("5.등급확인")
    print("6.합격유무확인")

    menu_number = input("원하는 메뉴의 번호를 선택하시오 :")
    if not (menu_number .isnumeric()) : #isnumeric = 숫자냐~
        menu_number = 99
    else:
        menu_number = int(menu_number)   
    return menu_number

def score_sum(new_list) :
    sum = 0
    for i in new_list:
        sum = sum + i
    return sum

def score_avg(new_list) :
#    sum = 0
#    for i in new_list:
#       sum = sum +i
#    avg = sum/len(new_list)
#    return avg  #5줄을 한줄로 변환할 수 있당
    return score_sum(new_list) / len(new_list)

def high_score(new_list) :
    max_no = -999
    for i in new_list :
        if max_no < i :
            max_no = i
    return max_no

def low_score(new_list) :
    min_no =999
    for i in new_list:
        if min_no > i:
            min_no = i
    return min_no

def grade_1(jumsoo) :
    if  jumsoo >= 90:
        grade = "A"
    elif jumsoo >=80:
        grade = "B"
    elif jumsoo >=70:
        grade = "C"
    elif jumsoo >=60:
        grade = "D"
    else :
        grade = "F"
    return grade

def grade_2(new_list):
    
    grade = [ ]
    for jumsoo in new_list:
            if  jumsoo >= 90:
                grade.append("A")
            elif jumsoo >=80:
                grade.append("B")
            elif jumsoo >=70:
                grade.append("C")
            elif jumsoo >=60:
                grade.append("D")
            else :
                grade.append("F")
    return grade 
            
# 메인 프로그램
kor_score = [94, 90, 45, 20, 80, 98, 75, 85, 69, 89]            # 10명의 국어 점수
math_score = [90, 85, 61, 49, 83, 93, 73, 55, 70, 99]          # 10명의 수학 점수
while True:
    number = choice_menu()
    
    if number == 0:
        print("프로그램을 종료합니다")
        break
    elif number == 1:
      #  print("합계점수를 구합니다")
        result_kor = score_sum(kor_score)
        result_math = score_sum(math_score)
        print("국어점수 합계 : %d   수학점수 합계 : %d" %(result_kor,result_math))
    elif number == 2:
      #   print("평균점수를 구합니다")
        avg_kor=score_avg(kor_score)
        avg_math=score_avg(math_score)
        print("국어점수 평균 : %4.1f    수학점수 평균 : %4.1f" %(avg_kor,avg_math))
    elif number == 3:
      #   print("최고점수를 구합니다")
        result_kor = high_score(kor_score)
        result_math = high_score(math_score)
        print("국어 점수 최댓값 : %3d      수학 점수 최댓값 : %3d"%(result_kor,result_math))
    elif number == 4:
       #  print("최저점수를 구합니다")
       result_kor = low_score(kor_score)
       result_math = low_score(math_score)
       print("국어 점수 최솟값 : %3d      수학 점수 최솟값 : %3d"%(result_kor,result_math))
    elif number == 5:
       #   print("등급을 확인합니다")
        for kor_jumsoo in kor_score :
            result_kor = grade_1(kor_jumsoo)
            print("점수 : %3d     등급 : %s"%(kor_jumsoo, result_kor))

        result_math = grade_2(math_score)
        print("점수 : ," ,math_score)
        print("등급 :",result_math)
       
    elif number == 6:
        print("합격 유무 확인합니다")
  
    else:
        print("잘못 입력하셨습니다.")
    print()
