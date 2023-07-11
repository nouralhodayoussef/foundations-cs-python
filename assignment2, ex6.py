#Question 6:
#Create a recursive function that takes a string s as a parameter and returns a string with all consecutive duplicate characters in s removed, so only one will be left.
#EX: if s= “hhellooo wwwwwoorldddd” then the function will return “helo world”

def remove_duplicates(s):
    if len(s) <= 1:
        return s

    if s[0] == s[1]:
        return remove_duplicates(s[1:])
    else:
        return s[0] + remove_duplicates(s[1:])
    
print(remove_duplicates("hiiii pythooonnnn"))