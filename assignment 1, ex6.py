num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num2 < num1:
    num1, num2 = num2, num1
print("Even numbers between", num1, "and", num2, ":")
for i in range(num1 + 1, num2):
    if i % 2 == 0:
        print(i, end=", ")