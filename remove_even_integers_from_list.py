"""
Challenge 1: Remove Even Integers from List
Given an array of size n, remove all even integers from it. Implement this solution in Python and see if it runs without an error.
Input
A list with random integers.

Output
A list with only odd integers

Sample Input
myList = [1,2,4,5,10,6,3]
Sample Output
myList = [1,5,3]
"""
import array

def remove_even_int(my_list):
    """ Constant space solution """
    length_list = len(my_list)
    i = 0
    # for i in range(len(my_list)):
    while(i < length_list):
        if my_list[i] %  2 == 0:            
            del my_list[i]
        else:
            i = i + 1
        length_list = len(my_list)
        # print(my_list)

    # return [i for i in range(length_list) if my_list[i] % 2 == 0] # solution with list comprehension
    return my_list

my_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list2 = [1, 2, 4, 5, 10, 6, 3]

print(remove_even_int(my_list1))
print(remove_even_int(my_list2))

print(remove_even_int(array.array('i', my_list1)))
print(remove_even_int(array.array('i', my_list2)))
