#Question 1:
#Create a function that takes a string s and an integer i as parameters and returns a string that has in it s reversed and concatenated i times.
# EX: if s is “hello” and i is 2, the function returns “olleholleh”. If i is 0, the function returns an empty string.

def reverseAndConcatenate(s, i):
    if i == 0:
        return ""

    reverse = s[::-1]
    concatenatedString = reverse * i

    return concatenatedString
s = input("Enter a string: ")
i = eval(input("Enter an integer: "))

print(reverseAndConcatenate(s, i))