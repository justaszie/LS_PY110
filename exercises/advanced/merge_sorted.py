"""
PROBLEM
- Input: sorted list of strings or integers
- Output: list containing elements from both input lists, in ascending order
- Rules:
    - Assuming both lists empty will result in empty list output
    - If one list is empty, the output will contain elements from the other list
    - Sorting can't be used
    - Result list must be built one element at a time
    - Input list should not be mutated
    - Lists may not have same lengths

[1, 5, 9], [2, 6, 8]
=>
iterate from 0 to the last index of the longer list.

if elements remain in list 1 or list 2:
    - find the minimum in both list, compare them, append the smaller one.

iterations:
- 0. minimum of list1, minimum of list 2, pop and append the one that is <.


ALGORITHM.
    1. Iterate indexes from 0 to sum(len(lst1), len(lst2))
    2. If there are elements in list 1 remaining:
        If there are elements in list 2 remaining:
            - compare the 1st element of list 1 to the 1st element of list 2.
                - Whichever is smaller is removed from the list and appended to result list.
        Else, append from list 1
    3. Else:
        if there are element in list 2 remaining:
            - append from list 2



test

[1, 1, 3], [2, 2]

iter 0:
1 < 2 | remove 1 from list 1, append to result. Result = [1] | [1,3], [2,2]
iter 1:
1 < 2 | remove 1, apend | Result [1, 1] | [3, 2, 2]
iter 2:
2 < 3 | remove and append 2 | Result [1, 1, 2] | [3], [2]
iter 3:
Same outcome | Result 1, 1, 2, 2 | [3] []
iter 4:
List 1 has elements.
List 2 has no elements => append 3
"""

def merge(lst1, lst2):
    result = []
    lst1_copy = lst1.copy()
    lst2_copy = lst2.copy()

    for _ in range(len(lst1_copy) + len(lst2_copy)):
        if lst1_copy:
            if lst2_copy:
                if lst1_copy[0] <= lst2_copy[0]:
                    result.append(lst1_copy.pop(0))
                else:
                    result.append(lst2_copy.pop(0))
            else:
                result.append(lst1_copy.pop(0))
        else:
            result.append(lst2_copy.pop(0))

    return result

  # All of these examples should print True
print(merge([1, 5, 9], [2, 6, 8]) == [1, 2, 5, 6, 8, 9])
print(merge([1, 1, 3], [2, 2]) == [1, 1, 2, 2, 3])
print(merge([], [1, 4, 5]) == [1, 4, 5])
print(merge([1, 4, 5], []) == [1, 4, 5])

names1 = ['Alice', 'Kim', 'Pete', 'Sue']
names2 = ['Bonnie', 'Rachel', 'Tyler']
names_expected = ['Alice', 'Bonnie', 'Kim', 'Pete',
                  'Rachel', 'Sue', 'Tyler']
print(merge(names1, names2) == names_expected)