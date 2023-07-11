#Question 4:
#Python has an inbuilt function called max() that returns the element with the maximum value.
#Create a function that does a very similar thing (without using the max() function). The function takes a list of numbers l as a parameter and returns the highest number in the list and its index.
#EX: if l = [5,6,3,2,7,2,0,1,6], the function should return “the highest value in the list is 7 at index 4”
#(BONUS: do the same but for the minimum)

def find_highest_value(l):
    if len(l) == 0:
        print("The list is empty.")
        return

    max_value = l[0]
    max_index = 0

    for i in range(1, len(l)):
        if l[i] > max_value:
            max_value = l[i]
            max_index = i

    print("The highest value in the list is", max_value, "at index", max_index, ".")


def find_lowest_value(l):
    if len(l) == 0:
        print("The list is empty.")
        return

    min_value = l[0]
    min_index = 0

    for i in range(1, len(l)):
        if l[i] < min_value:
            min_value = l[i]
            min_index = i

    print("The lowest value in the list is", min_value, "at index", min_index, ".")

l = [5, 6, 3, 2, 7, 2, 0, 1, 6]
find_highest_value(l)  
find_lowest_value(l) 