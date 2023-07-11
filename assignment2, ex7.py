#Question 7 (optional):
#Create a recursive function that takes an integer parameter n which returns the positive integer that you get when you reverse the digits of parameter n.
#EX: if n=12345 the function would return 54321.

def reverse_digits(n, reverse=0):
    if n == 0:
        return reverse
    else:
        remainder = n % 10
        reverse = 10 * reverse + remainder
        return reverse_digits(n // 10, reverse)
    
print(reverse_digits(1234))