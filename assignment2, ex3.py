#Question 3:
#Create a function that takes two strings s1 and s2 as parameters and returns True if s1 is a reordering of the characters in s2.
#EX: if s1=”abcde” and s2=”edacb” , the function returns True. If s1=”aabc” and s2=”edabc”, the function returns False.

def isReordering(s1, s2):
    if len(s1) != len(s2):
        return False

    sorted_s1 = sorted(s1)
    sorted_s2 = sorted(s2)

    return sorted_s1 == sorted_s2
print(isReordering("abcde", "edacb"))