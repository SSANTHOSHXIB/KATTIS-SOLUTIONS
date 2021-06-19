num1, num2 = input().split()
num1 = int(num1)
num2 = int(num2)
print((str(num2) + " " + str(num1)) if num2 < num1 else (str(num1) + " " + 
str(num2)))
