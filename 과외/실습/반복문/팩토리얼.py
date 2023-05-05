num = int(input('정수를 입력하세요 : '))

fac = 1
for i in range(1,num+1):
    fac = fac*i
   
print('팩토리얼 값은 %d 입니다.'%fac)   