#Question 2:
#Create a function that takes a string s as a parameter and returns another string where all the letters in s has been re-arranged such that upper case letters appear before the lower case letters.
#EX: if s is “Hello World”, the function returns “HWelloorld”.

def rearrangeLetters(s):
    upperCase = ""
    lowerCase = ""

    for char in s:
        if 'A' <= char <= 'Z':
            upperCase += char
        elif 'a' <= char <= 'z':
            lowerCase += char

    return upperCase + lowerCase
s = input("Enter a string: ")
print(rearrangeLetters(s))