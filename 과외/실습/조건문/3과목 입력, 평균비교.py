s1 = int(input("첫번째 숫자를 입력하세요 : "))
s2 = int(input("두번째 숫자를 입력하세요 : "))
s3 = int(input("세번째 숫자를 입력하세요 : "))

avg = (s1+s2+s3)/3

print(avg)

if avg>=60:
    print('합격')
else:
    print('불합격')