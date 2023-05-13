# writedata.py
f=open('새파일.txt','w') # 생성

for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

f = open("새파일.txt", 'r')
print(f.readline())
f.close()