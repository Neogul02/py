num = int(input())
print("주사위 3개의 합 : %d" % num)
for i in range(1, 7):
    for j in range(1, 7):
        for k in range(1, 7):  # 주사위 세번,
            if i + j + k == num:
                print("(%d,%d,%d)-" % (i, j, k), end="")
