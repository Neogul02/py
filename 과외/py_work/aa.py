for line in range(1 ,11,1):
    for i in range(1,(line-1)*2+1,1):
        print(" ",end="")
    for j in range(1,22-(line*2),1):
        print("o",end="")
    print()
