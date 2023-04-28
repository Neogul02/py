import random

number_1 = random.randint(1,10)
number_2 = random.randint(1,10)
a= "%"

print("1. 덧셈")
print("2. 뺄셈")
print("3. 곱셈")
print("4. 나눗셈")
print("5. 몫")
print("6. 나머지")

menu = int(input("메뉴선택(1~6) : "))

if menu == 1 :
    result = number_1 + number_2
    print("%d + %d = ? " %(number_1, number_2))
    
elif menu == 2 :
    result = number_1 - number_2
    print("%d - %d = ? " %(number_1, number_2))
       
elif menu == 3 :
    result = number_1 * number_2
    print("%d * %d = ? " %(number_1, number_2))
        
elif menu == 4 :
    result = number_1 / number_2
    print("%d / %d = ? " %(number_1, number_2))
    
elif menu == 5 :
    result = number_1 // number_2
    print("%d // %d = ? " %(number_1, number_2))
    
else:
    result = number_1 % number_2
    print("%d %c %d = ? " %(number_1, a, number_2))
    
input_result = int(input("정답을 입력하시오 : "))

if input_result == result :
    print("정답입니다")
else :
    print("정답이 아닙니다")




    
