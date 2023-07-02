num = eval(input("Enter a number: "))
digit = 0
while num != 0:
    rem = num % 10
    digit += 1
    num //= 10  # Assign the updated value of num to num itself
print("The number of digits is", digit)