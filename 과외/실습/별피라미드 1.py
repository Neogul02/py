line = int(input('몇 줄 출력할까요? : '))

for i in range(1,line+1): #1~
    for j in range(i): #
        print('*', end='')
    print('', end='\n')