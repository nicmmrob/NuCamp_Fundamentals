
x = 0

while x != 10:
    x += 1
    if x < 5:
        print(x)
    elif x == 6:
        print(x)
        continue
    elif x >= 5 and x <= 8:
        print("x is greater than or equal to 5, and less than or equal to 8, but not 6. It is:", x)
    else:
        print("x is greater than 8. It is:", x)
