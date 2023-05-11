# for 변수 in 리스트(도는 튜플, 문자열):
#   수행할 문장 1
#   수행할 문장 2

test_list = ["one", "two", "three"]
for i in test_list:
    print(i)


a = [(1, 2), (3, 4), (5, 6)]
for first, last in a:
    print(first + last)

# 총 5명의 학생이 시험을 보았는데 시험 점수가 60점 이상이면 합격이고 그렇지 않으면 불합격이다.
# 합격인지 불합격인지 결과를 보여 주시오.

score = [100, 90, 50, 70, 45]
cnt = 0
for i in score:
    cnt += 1
    if i >= 60:
        print("%d번 학생은 합격입니다." % cnt)
    else:
        print("%d번 학생은 불합격입니다." % cnt)
