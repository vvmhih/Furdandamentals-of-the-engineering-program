num1 = int(input())
num2 = int(input())
if 1 < (num1 or num2) < 1000:
    result = [num1, num2][num1 <= num2]
    print(result)
else:
    print("The numbers are not included in the range")