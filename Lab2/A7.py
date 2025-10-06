x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if ((x1 % y1 == 0) and (x2 % y2 == 0)):
    print("YES")
    print("White")
elif ((x1 % y1 == 1) and (x2 % y2 == 1)):
    print("YES")
    print("Black")
else:
    print("NO")