def getDigitCount(num):
    if num == 0:
        return 1
    count = 0
    while(num != 0):
        count += 1
        num //= 10
    return count
count = int(input())
for _ in range(count):
    print(getDigitCount(int(input())))
