


num=int(input())
if num < 10000000:
    if num % 7 == 2:
        print(10000003)
    elif num % 7 == 1:
        print(10000002)
    elif num % 7 == 0:
        print(10000001)
    elif num % 7 == 6:
        print(10000000)
    elif num % 7 == 5:
        print(9999999)
    elif num % 7 == 4:
        print(9999998)
    elif num % 7 == 3:
        print(9999997)
else:
    print(num-3)

    