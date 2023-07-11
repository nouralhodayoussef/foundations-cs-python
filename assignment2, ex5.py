#Question 5:
#Create a recursive function that takes an integer parameter n and returns the sum of its digits.
#EX: if n=348 the function should return 15 (3+4+8 = 15)
#HINT: you should use % and //

def sum_of_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_of_digits(n // 10)
    
num = eval(input("Enter a number: "))
print(sum_of_digits(num))