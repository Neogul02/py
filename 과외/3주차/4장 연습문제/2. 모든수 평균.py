def avg(*n):
    result = 0
    for i in n:
        result += i
    return result / len(n)


print(avg(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
