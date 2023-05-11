## while <조건문>:
#     <수행할 문장1>
#     <수행할 문장2>
#     <수행할 문장3>
#     ...

treeHit = 0
while True:
    print("나무를 %d번 찍었습니다." % treeHit)
    treeHit += 1
    if treeHit == 10:
        print("나무가 쓰러집니다")
        break


prompt = """
... 1. Add
... 2. Del
... 3. List
... 4. Quit
...
... Enter number: """

number = 0
while number != 4:
    print(prompt)
    number = int(input())


coffee = 10
money = 300

while money:
    print("돈을 받았습니다 커피를 드릴게요!")
    coffee = coffee - 1
    print("남은 커피의 양은 %d개 입니다." % coffee)
    if coffee == 0:
        print("커피가 없습니다 ㅠㅠ")
