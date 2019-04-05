"""
Challenge 2: Merge Two Sorted Lists
Given two sorted lists, merge them into one list which should also be sorted. Implement the solution in Python and see if your code runs successfully!
Input:
Two sorted lists.

Output:
A merged and sorted list consisting of all elements of both input lists.

Sample Input
arr1 = [1,3,4,5]  
arr2 = [2,6,7,8]
Sample Output
arr = [1,2,3,4,5,6,7,8]
"""

def merge_two_sorted_lists(list_a, list_b):
    i = 0
    j = 0
    
    new_list = []
    l = len(list_a) + len(list_b)

    while(i + j < l):
        # print(i, j)
        if i > len(list_a) - 1:
            new_list.append(list_b[j])
            j = j + 1
            continue

        if j > len(list_b) - 1:
            new_list.append(list_a[j])
            i = i + 1
            continue
            
        if list_a[i] < list_b[j]:
            new_list.append(list_a[i])
            i = i + 1
        elif list_b[j] < list_a[i]:
            new_list.append(list_b[j])
            j = j + 1
        else: # must be equal
            new_list.append(list_a[i])
            new_list.append(list_b[j])
            i = i + 1
            j = j + 1

    return new_list
        
arr1 = [1,3,4,5]  
arr2 = [2,6,7,8]
print(merge_two_sorted_lists(arr1, arr2))

arr1 = [1,3,3,3]  
arr2 = [2,3,3,3]
print(merge_two_sorted_lists(arr1, arr2))

arr1 = [1, 7, 9, 12, 22, 30]  
arr2 = [2, 4, 9, 13, 33, 33, 39, 40, 51, 51]
print(merge_two_sorted_lists(arr1, arr2))




