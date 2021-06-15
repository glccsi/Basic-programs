num1 = int(input())
num2 = int(input())
num3 = int(input())
summa = num1 + num2 + num3
result = summa // 2

if summa % 2 == 0:
    print(result)
else:
    print(result + 1)