"""
PROBLEM
- Input: List of either strings or integers
- Output: New list of elements sorted using merge-sort algo
- Rules:
    - First, split the elements lists into sub-lists of 1 element each (dividing into sublists until each sublist is 1 elem)
    - Can use 'merge' function that merges sorted lists


ALGORITHM
[!] 1. Divide the list into sublists until each sublist has 1 element
[!] 2. Apply merge algo on each pair of sublists until there are no sublists

[1, 7, 5]
=> [1, 7], [5]
=> []
=> [[1], [7], [5]]

[!] Dividing
1. Divide the list into sublists
    A. Set middle index to len(list) // 2
    B. return a list with 2 sub-lists.
        - indexes 0:middle_index + 1
        - indexes middle_index+1:len(list)
3. Iterate over the sublists. For each sublist:
    1. If it contains 1 element, do nothing
    2. If it contains more than 1 element, apply step 1 to it.

[!] Merging
1.



"""
def merge_sort(lst):
    # splitted = to_sublists(lst)
    # flattened = flatten(splitted)

    return flatten(to_sublists(lst))

def to_sublists(lst):
    middle_index = len(lst) // 2
    left, right = lst[0:middle_index], lst[middle_index: len(lst)]
    if len(left) > 1:
        left = to_sublists(left)
    if len(right) > 1:
        right = to_sublists(right)

    return [left, right]

def flatten(lst):
    left, right = lst
    if len(left) > 1:
        left = flatten(left)
    if len(right) > 1:
        right = flatten(right)

    return merge(left, right)

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
print(merge_sort([9, 5, 7, 1]) == [1, 5, 7, 9])
print(merge_sort([5, 3]) == [3, 5])
print(merge_sort([6, 2, 7, 1, 4]) == [1, 2, 4, 6, 7])
print(merge_sort([9, 2, 7, 6, 8, 5, 0, 1]) == [0, 1, 2, 5, 6, 7, 8, 9])

original = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
            'Kim', 'Bonnie']
expected = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel',
            'Sue', 'Tyler']
print(merge_sort(original) == expected)

original = [7, 3, 9, 15, 23, 1, 6, 51, 22, 37, 54,
            43, 5, 25, 35, 18, 46]
expected = [1, 3, 5, 6, 7, 9, 15, 18, 22, 23, 25,
            35, 37, 43, 46, 51, 54]
print(merge_sort(original) == expected)