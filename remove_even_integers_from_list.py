"""
Challenge 1: Remove Even Integers from List
Given an array of size n, remove all even integers from it. Implement this solution in Python and see if it runs without an error.
"""

def remove_even_int(my_list):
    length_list = len(my_list)
    for i in range(len(my_list)):
        if i < length_list and my_list[i] %  2 == 0:            
            del my_list[i]
        length_list = len(my_list)

    return my_list

print(remove_even_int([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))