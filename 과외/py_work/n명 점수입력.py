# 6-13 n 명의 점수 입력하기

#n = int(input("학생수를 입력하세요 : "))
s_jumsoo = []
jumsoo = 11
i = 1
while True : 
        print(i, end = " ")
        jumsoo = input(" 번째 학생의 점수를 입력하십시오 : ")

        if jumsoo == "" :
            break
 
        s_jumsoo.append(int(jumsoo))
        i=i+1
        
print(s_jumsoo)        


#6-14 n명의 점수에 대한 합계와 평균
#합
sum=0
for i in s_jumsoo :
    sum += i   

#평균
avg= sum / len(s_jumsoo)

print("합계 : %d   평균 : %.2f"%(sum,avg)) #소숫점 둘째 %.2f

#6-15 n명의 점수에 대한 최댓값과 최솟값
max_no = -999
min_no = 999

for i in s_jumsoo :
    if max_no < i :
        max_no = i
    if min_no > i :
        min_no = i

print("최댓값 : %d   최솟값 : %d"%(max_no,min_no))

        
